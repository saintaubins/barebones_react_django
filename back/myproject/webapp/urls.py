from rest_framework import routers
from .api import LeadViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/employees', EmployeeViewSet, 'employees')


urlpatterns = router.urls
