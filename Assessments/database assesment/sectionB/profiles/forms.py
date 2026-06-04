from django import forms
from .models import UserProfile


# Task 2 — ModelForm with custom validation
# UserProfileForm is tied to the UserProfile model so Django auto-generates
# the form fields (username, age, is_public) for us.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'is_public']   # all three model fields

    # Custom validation: the user must be older than 13
    # Django calls clean_<fieldname>() automatically during form.is_valid()
    def clean_age(self):
        age = self.cleaned_data.get('age')           # get the value already type-checked by IntegerField
        if age is not None and age < 13:
            raise forms.ValidationError("User must be at least 13 years old to create a profile.")
        return age                                   # always return the cleaned value
