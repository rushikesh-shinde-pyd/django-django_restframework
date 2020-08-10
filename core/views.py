# Django imports
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Django Rest-framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local imports
from core.models import Employee
from core.serializers import EmpSerializer


# Class Based views
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeList(APIView):
    def get(self, request, format=None):
        serializer = EmpSerializer(Employee.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetail(APIView):
    def get_object(self, pk):
        print(pk)
        return get_object_or_404(Employee, pk=pk)

    def get(self, request, format=None, **kwargs):
        serializer = EmpSerializer(self.get_object(kwargs.get('pk')))
        return Response(serializer.data)

    def put(self, request, format=None, **kwargs):
        serializer = EmpSerializer(self.get_object(kwargs.get('pk')), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, **kwargs):
        employee = self.get_object(kwargs.get('pk'))
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function Based views
    # here  
