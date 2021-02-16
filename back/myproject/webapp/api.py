from . models import Lead, employee
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, employeeSerializer

# Lead Viewset functionality for the CRUD

class LeadViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LeadSerializer
    
    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = employeeSerializer
