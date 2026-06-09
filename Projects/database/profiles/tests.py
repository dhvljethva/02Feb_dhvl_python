from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import UserProfile
from .forms import UserProfileForm

class UserProfileTests(TestCase):
    def setUp(self):
        # Create a default profile
        self.profile = UserProfile.objects.create(
            username="testuser",
            age=20,
            is_public=True
        )

    def test_profile_creation(self):
        """Asserts that a profile object can be successfully created and stored."""
        self.assertEqual(self.profile.username, "testuser")
        self.assertEqual(self.profile.age, 20)
        self.assertTrue(self.profile.is_public)
        self.assertEqual(str(self.profile), "testuser")

    def test_form_validation_valid_age(self):
        """Asserts that the form is valid when age is 13 or older."""
        data = {
            'username': 'newuser',
            'age': 13,
            'is_public': True
        }
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_invalid_age(self):
        """Asserts that the form is invalid when age is less than 13."""
        data = {
            'username': 'younguser',
            'age': 12,
            'is_public': True
        }
        form = UserProfileForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)
        self.assertEqual(
            form.errors['age'][0], 
            "You must be at least 13 years old to create a profile."
        )

    def test_form_validation_negative_age(self):
        """Asserts that the form is invalid when age is negative."""
        data = {
            'username': 'negativeuser',
            'age': -5,
            'is_public': True
        }
        form = UserProfileForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)

    def test_profile_list_view_without_search(self):
        """Asserts that the view renders all profiles correctly with standard GET request."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "@testuser")

    def test_profile_list_view_search_match(self):
        """Asserts that the view filters profiles when search query is passed."""
        UserProfile.objects.create(username="otheruser", age=30, is_public=True)
        response = self.client.get('/?q=other')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "@otheruser")
        self.assertNotContains(response, "@testuser")

    def test_profile_list_view_search_no_match(self):
        """Asserts that clear warning/empty message shows up when no profile matches search query."""
        response = self.client.get('/?q=nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No matching profiles found")

    def test_profile_list_pagination(self):
        """Asserts that the view paginates entries (5 items per page)."""
        # Create 6 more profiles to make total = 7
        for i in range(6):
            UserProfile.objects.create(username=f"user_{i}", age=20+i, is_public=True)
        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Page 1 should contain 5 items, not all 7
        profiles_on_page = response.context['profiles']
        self.assertEqual(len(profiles_on_page), 5)
        
        # Access page 2
        response_page2 = self.client.get('/?page=2')
        self.assertEqual(response_page2.status_code, 200)
        self.assertEqual(len(response_page2.context['profiles']), 2)

