from django.shortcuts import render
from rest_framework import viewsets
from . serializers import Userserializer
from . models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = Userserializer
