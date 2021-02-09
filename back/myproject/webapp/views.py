from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404  # if the route doesn't exist
from rest_framework.views import APIView
from rest_framework.response import Response   # will return the 200, 400, etc... 
from rest_framework import status
from . models import employee
from . serializers import employeeSerializer

class employeeList(APIView):  # inherits from APIView

    def get(self, request):
        employee1 = employee.objects.all()
        serializer = employeeSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(self):
        pass




