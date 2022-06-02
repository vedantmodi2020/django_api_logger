from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets , permissions
from test_app1.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
