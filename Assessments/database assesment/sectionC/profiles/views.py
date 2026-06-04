import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm


# LIST VIEW – fetches all profiles from the database and displays them
def profile_list(request):
    profiles = Profile.objects.all().order_by('-created_at')
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})


# CREATE VIEW – shows a blank form, validates input, and saves a new profile
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile_form.html', {'form': form, 'title': 'Create Profile'})


# EDIT VIEW – loads an existing profile into the form for editing
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_form.html', {'form': form, 'title': 'Edit Profile'})


# EXPORT VIEW – uses context manager to write all profiles into a CSV file
def profile_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    # Using context manager (with ... as file) for safe file handling
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone', 'Bio', 'City', 'Created At'])

    profiles = Profile.objects.all()
    for profile in profiles:
        writer.writerow([
            profile.first_name,
            profile.last_name,
            profile.email,
            profile.phone,
            profile.bio,
            profile.city,
            profile.created_at,
        ])

    return response
