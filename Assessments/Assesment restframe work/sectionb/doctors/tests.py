from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from .models import Doctor

class DoctorAPITests(APITestCase):
    def setUp(self):
        # Create doctors for testing list, pagination, and ordering
        self.doc1 = Doctor.objects.create(name="Dr. Smith", specialization="Cardiology", city="New York")
        self.doc2 = Doctor.objects.create(name="Dr. Doe", specialization="Pediatrics", city="Chicago")
        self.doc3 = Doctor.objects.create(name="Dr. Adams", specialization="Dermatology", city="Boston")
        self.doc4 = Doctor.objects.create(name="Dr. Taylor", specialization="Neurology", city="Miami")
        self.doc5 = Doctor.objects.create(name="Dr. Wilson", specialization="Oncology", city="Houston")
        self.doc6 = Doctor.objects.create(name="Dr. Johnson", specialization="General Medicine", city="Seattle")
        self.list_url = reverse('doctor-list')

    def test_create_doctor(self):
        """Test POST /api/doctors/ creates a doctor successfully."""
        data = {
            "name": "Dr. House",
            "specialization": "Diagnostic Medicine",
            "city": "Princeton"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Dr. House")
        self.assertTrue(Doctor.objects.filter(name="Dr. House").exists())

    def test_list_doctors_limit_offset_pagination(self):
        """Test GET /api/doctors/ with limit and offset parameters."""
        response = self.client.get(self.list_url, {'limit': 2, 'offset': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify pagination keys
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertIn('results', response.data)
        self.assertEqual(response.data['count'], 6)
        self.assertEqual(len(response.data['results']), 2)
        # Since default ordering is by id, offset=1 should return the 2nd and 3rd doctors (doc2, doc3)
        self.assertEqual(response.data['results'][0]['name'], self.doc2.name)
        self.assertEqual(response.data['results'][1]['name'], self.doc3.name)

    def test_retrieve_doctor(self):
        """Test GET /api/doctors/<id>/ returns doctor details."""
        url = reverse('doctor-detail', kwargs={'pk': self.doc1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.doc1.name)

    def test_update_doctor(self):
        """Test PUT /api/doctors/<id>/ updates a doctor."""
        url = reverse('doctor-detail', kwargs={'pk': self.doc1.pk})
        data = {
            "name": "Dr. Smith Jr.",
            "specialization": "Cardiology",
            "city": "Boston"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Dr. Smith Jr.")
        self.assertEqual(response.data['city'], "Boston")

    def test_delete_doctor(self):
        """Test DELETE /api/doctors/<id>/ deletes a doctor."""
        url = reverse('doctor-detail', kwargs={'pk': self.doc1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Doctor.objects.filter(pk=self.doc1.pk).exists())

    def test_ordering_by_name_ascending(self):
        """Test ordering doctors by name in ascending order."""
        response = self.client.get(self.list_url, {'ordering': 'name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Sorted names: Adams, Doe, Johnson, Smith, Taylor, Wilson
        results = response.data['results']
        names = [doc['name'] for doc in results]
        self.assertEqual(names, ["Dr. Adams", "Dr. Doe", "Dr. Johnson", "Dr. Smith", "Dr. Taylor"])

    def test_ordering_by_name_descending(self):
        """Test ordering doctors by name in descending order."""
        response = self.client.get(self.list_url, {'ordering': '-name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Sorted names desc: Wilson, Taylor, Smith, Johnson, Doe, Adams
        results = response.data['results']
        names = [doc['name'] for doc in results]
        self.assertEqual(names, ["Dr. Wilson", "Dr. Taylor", "Dr. Smith", "Dr. Johnson", "Dr. Doe"])

    def test_ordering_by_specialization(self):
        """Test ordering doctors by specialization."""
        response = self.client.get(self.list_url, {'ordering': 'specialization'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        specializations = [doc['specialization'] for doc in results]
        # Alphabetic: Cardiology (Smith), Dermatology (Adams), General Medicine (Johnson), Neurology (Taylor), Oncology (Wilson), Pediatrics (Doe)
        # Page size is 5, so first 5: Cardiology, Dermatology, General Medicine, Neurology, Oncology
        self.assertEqual(specializations, ["Cardiology", "Dermatology", "General Medicine", "Neurology", "Oncology"])

    def test_create_doctor_atomic_rollback(self):
        """Verify that if an exception occurs during doctor creation, the database rolls back."""
        data = {
            "name": "Dr. Rollback",
            "specialization": "Pediatrics",
            "city": "Boston"
        }
        # Patch Doctor.save to raise an exception to simulate database write failure
        with patch.object(Doctor, 'save', side_effect=Exception("Database error")):
            with self.assertRaises(Exception):
                self.client.post(self.list_url, data, format='json')
        
        # Check that the doctor was NOT created in the database
        self.assertFalse(Doctor.objects.filter(name="Dr. Rollback").exists())

    def test_update_doctor_atomic_rollback(self):
        """Verify that if an exception occurs during doctor update, the database rolls back."""
        url = reverse('doctor-detail', kwargs={'pk': self.doc1.pk})
        data = {
            "name": "Dr. Smith Jr.",
            "specialization": "Cardiology",
            "city": "Boston"
        }
        # Patch Doctor.save to raise an exception
        with patch.object(Doctor, 'save', side_effect=Exception("Database error")):
            with self.assertRaises(Exception):
                self.client.put(url, data, format='json')
        
        # Re-fetch from database to verify it remains unchanged
        self.doc1.refresh_from_db()
        self.assertEqual(self.doc1.name, "Dr. Smith")
        self.assertEqual(self.doc1.city, "New York")
