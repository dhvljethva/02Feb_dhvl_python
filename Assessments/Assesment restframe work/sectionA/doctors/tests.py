from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.db import transaction
from .models import Doctor

class DoctorAPITests(APITestCase):
    def setUp(self):
        # Create a few doctors for testing pagination and retrieve
        self.doc1 = Doctor.objects.create(name="Dr. Smith", specialization="Cardiology", city="New York")
        self.doc2 = Doctor.objects.create(name="Dr. Doe", specialization="Pediatrics", city="Chicago")
        self.doc3 = Doctor.objects.create(name="Dr. Adams", specialization="Dermatology", city="Boston")
        self.doc4 = Doctor.objects.create(name="Dr. Taylor", specialization="Neurology", city="Miami")
        self.doc5 = Doctor.objects.create(name="Dr. Wilson", specialization="Oncology", city="Houston")
        self.doc6 = Doctor.objects.create(name="Dr. Johnson", specialization="General Medicine", city="Seattle")
        self.list_url = reverse('doctor-list')

    def test_list_doctors_paginated(self):
        """Test GET /api/doctors/ returns a paginated list of doctors."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify pagination structure
        self.assertIn('count', response.data)
        self.assertIn('results', response.data)
        self.assertEqual(response.data['count'], 6)
        # Page size is 5, so we should get 5 doctors on the first page
        self.assertEqual(len(response.data['results']), 5)

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
        # Check that the object exists in database
        self.assertTrue(Doctor.objects.filter(name="Dr. House").exists())

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
