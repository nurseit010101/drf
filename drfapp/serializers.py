from dataclasses import field
from rest_framework import serializers


from drfapp.models import Students




class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'course']