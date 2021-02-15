from . models import Lead, employee
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, employeeSerializer

# Lead Viewset functionality for the CRUD

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = employeeSerializer
