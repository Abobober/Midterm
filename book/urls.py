from django.urls import path
from .views import ContactDetailView, ContactView, ContactCreateView

urlpatterns = [
path('', ContactView.as_view(), name='contact_list'),
path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
path('contact/new/', ContactCreateView.as_view(), name='contact_new'),
]