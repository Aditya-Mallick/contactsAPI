from django.urls import path
from .views import *


urlpatterns = [
  path('', ContactListView.as_view(), name='contact-list'),
  path('<int:id>/', ContactDetailView.as_view(), name='contact-detail'),
]