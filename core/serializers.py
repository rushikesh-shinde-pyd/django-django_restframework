from rest_framework import serializers
from .import models


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Employee

