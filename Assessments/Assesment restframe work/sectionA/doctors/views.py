from rest_framework import viewsets
from django.db import transaction
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()
