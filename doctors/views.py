from django.shortcuts import render
from .models import Doctors
from rest_framework import generics
from .serializers import DoctorsSerializer
from django.http import JsonResponse

class ListDoctorsView(generics.ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

def doctors_list(request):
    MAX_OBJECTS = 20
    doctors = Doctors.objects.all()[:MAX_OBJECTS]
    data = list(doctors.values("id","first_name", "last_name", "profile_image"))
    return JsonResponse(data, safe=False)
