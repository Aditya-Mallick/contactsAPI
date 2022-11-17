from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class Home(APIView):
  def get(self, request):
    return Response({
      'swagger': 'swagger/',
      'register': 'api/auth/register/',
      'token': 'api/auth/token/',
      'list/create': 'api/contacts/',
      'retrive, update or delete': 'api/contacts/<int:id>/'
    })



class ContactListView(ListCreateAPIView):
  serializer_class = ContactSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  def get_queryset(self):
    return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
  serializer_class = ContactSerializer
  permission_classes = [permissions.IsAuthenticated]
  lookup_field = 'id'

  def get_queryset(self):
    return Contact.objects.filter(owner=self.request.user)