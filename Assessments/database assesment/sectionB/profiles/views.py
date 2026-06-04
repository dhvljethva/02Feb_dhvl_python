from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile


# Task 3 — Function-based view to handle profile creation
# GET  → show an empty form
# POST → validate and save if valid, otherwise re-show form with errors
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)     # bind the submitted data to the form
        if form.is_valid():                       # runs all field validations + clean_age()
            form.save()                           # saves the new UserProfile row to the database
            return redirect('profile_list')       # after saving, go to the list page
    else:
        form = UserProfileForm()                  # empty form for GET request

    return render(request, 'profiles/create_profile.html', {'form': form})


# Task 4 — View that fetches all profiles and sends them to the template
def profile_list(request):
    profiles = UserProfile.objects.all()          # SELECT * FROM profiles_userprofile
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})
