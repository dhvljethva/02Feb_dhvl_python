from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'is_public']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your unique username',
                'id': 'id_username'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age',
                'id': 'id_age'
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'id_is_public'
            }),
        }
        labels = {
            'username': 'Username',
            'age': 'Age',
            'is_public': 'Make Profile Public (visible to everyone)',
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        
        # Enforce beginner-friendly simple validation logic
        if age is not None:
            if age < 0:
                raise forms.ValidationError("Age cannot be a negative number.")
            if age < 13:
                raise forms.ValidationError("You must be at least 13 years old to create a profile.")
        
        return age
