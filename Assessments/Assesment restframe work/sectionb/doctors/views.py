from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from django.db import transaction
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing doctor profiles.
    Supports LimitOffsetPagination and OrderingFilter.
    Uses atomic transactions for sensitive database modifications.
    """
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'specialization', 'city']
    ordering = ['id']  # Default stable ordering

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

    def perform_update(self, serializer):
        with transaction.atomic():
            serializer.save()

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.delete()
