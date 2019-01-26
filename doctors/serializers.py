from rest_framework import serializers
from .models import Doctors


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ("first_name", "last_name","profile_image")
