from django.shortcuts import render
from .models import Doctors
from rest_framework import generics
from .serializers import DoctorsSerializer

def doctors_list(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'doctors.html', context)

class ListDoctorsView(generics.ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
