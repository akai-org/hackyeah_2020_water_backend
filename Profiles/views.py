from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Profiles.serializers import ProfileSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from Profiles.models import Profile


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
