from django.urls import path
from .views import *

urlpatterns = [
    path('', profile, name='my_profile'),
    path('update/profile', update_profile, name='my_profile_update'),
    path('update/contact', update_contact, name='my_contact_update'),
]
