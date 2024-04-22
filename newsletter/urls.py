from django.urls import path
from .views import newsletter_signup, newsletter_confirmation

urlpatterns = [
    path('signup/', newsletter_signup, name='newsletter_signup'),
    path('confirmation/', newsletter_confirmation, name='newsletter_confirmation'),
]


