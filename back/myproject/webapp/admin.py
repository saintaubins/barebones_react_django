from django.contrib import admin

from . models import employee, Lead

admin.site.register(employee)
admin.site.register(Lead)

# works without this page
