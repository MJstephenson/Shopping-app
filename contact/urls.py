from django.urls import path
from .views import contact_view, thank_you_view  # Correctly import the views

urlpatterns = [
    path('', contact_view, name='contact'),  # URL for the contact form
    path('thank-you/', thank_you_view, name='thank_you'),  # URL for the thank you page
]