from rest_framework import serializers


from . models import employee, Lead

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        # fields = ('firstname', 'lastname')  if you want to be specific
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'