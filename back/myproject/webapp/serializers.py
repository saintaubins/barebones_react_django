from rest_framework import serializers

# from rest_framework import employee

from . models import employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        # fields = ('firstname', 'lastname')  if you want to be specific
        fields = '__all__'