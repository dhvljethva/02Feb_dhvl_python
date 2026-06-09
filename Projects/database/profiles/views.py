import os
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import FileResponse, Http404
from django.contrib import messages
from django.db.models import Avg
from django.core.paginator import Paginator
from .models import UserProfile
from .forms import UserProfileForm

def profile_list(request):
    """
    View to retrieve UserProfiles and pass them to the dashboard template.
    Supports query search/filtering and list pagination.
    Also calculates dynamic database-wide stats for visual impact.
    """
    # 1. Dashboard statistics remain database-wide to show the full ecosystem health
    all_profiles = UserProfile.objects.all().order_by('id')
    total_count = all_profiles.count()
    public_count = all_profiles.filter(is_public=True).count()
    private_count = total_count - public_count
    
    # Calculate average age using Django ORM aggregation
    avg_age = 0
    if total_count > 0:
        avg_data = all_profiles.aggregate(Avg('age'))
        avg_age = round(avg_data['age__avg'] or 0, 1)
        
    # 2. Extract search term and filter profiles list
    query = request.GET.get('q', '').strip()
    if query:
        filtered_profiles = all_profiles.filter(username__icontains=query)
    else:
        filtered_profiles = all_profiles
        
    # 3. Paginate the filtered profile listings (5 per page)
    paginator = Paginator(filtered_profiles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'profiles': page_obj,  # Django template iterates over the page object
        'total_count': total_count,
        'public_count': public_count,
        'private_count': private_count,
        'avg_age': avg_age,
        'query': query,
    }
    return render(request, 'profiles/profile_list.html', context)

def profile_create(request):
    """
    Handles creating a new profile. Validates age limit >= 13.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile for '{form.cleaned_data['username']}' created successfully!")
            return redirect('profile_list')
        else:
            messages.error(request, "Failed to create profile. Please check the errors below.")
    else:
        form = UserProfileForm()
        
    return render(request, 'profiles/profile_form.html', {
        'form': form,
        'title': 'Create New Profile',
        'button_text': 'Save Profile',
        'is_edit': False
    })

def profile_edit(request, pk):
    """
    Handles editing an existing profile record.
    """
    profile = get_object_or_404(UserProfile, pk=pk)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile for '{profile.username}' updated successfully!")
            return redirect('profile_list')
        else:
            messages.error(request, "Failed to update profile. Please verify your edits.")
    else:
        form = UserProfileForm(instance=profile)
        
    return render(request, 'profiles/profile_form.html', {
        'form': form,
        'title': f"Edit Profile: {profile.username}",
        'button_text': 'Update Changes',
        'is_edit': True,
        'profile': profile
    })

def profile_delete(request, pk):
    """
    Deletes a profile safely using POST request protection.
    """
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        username = profile.username
        profile.delete()
        messages.success(request, f"Profile '{username}' was permanently deleted.")
    return redirect('profile_list')

def export_profiles_csv(request):
    """
    Uses Python's csv module and a secure Context Manager (`with open(...) as file:`)
    to write profile records into a temporary CSV file on the server,
    then delivers that file directly to the browser for download.
    """
    # 1. Ensure the export directory exists inside our Django base directory
    export_dir = os.path.join(settings.BASE_DIR, 'exports')
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
        
    csv_file_path = os.path.join(export_dir, 'profiles_export.csv')
    
    # 2. Fetch all profiles from the database using Django ORM
    profiles = UserProfile.objects.all()
    
    # 3. Context Manager: Safe file opening, writing and automatic closing
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write headers
        writer.writerow(['Profile ID', 'Username', 'Age', 'Visibility Status'])
        
        # Write database entries
        for p in profiles:
            visibility = 'Public' if p.is_public else 'Private'
            writer.writerow([p.id, p.username, p.age, visibility])
            
    # 4. Read the safely written file and return it as a downloadable file response
    if os.path.exists(csv_file_path):
        # Open in binary read mode to stream it
        file_handle = open(csv_file_path, 'rb')
        response = FileResponse(file_handle, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="profiles_export.csv"'
        return response
        
    raise Http404("Export file could not be generated.")
