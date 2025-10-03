from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='discuss_home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]
