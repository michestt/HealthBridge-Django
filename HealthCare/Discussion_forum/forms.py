from django.forms import ModelForm
from .models import *
from django import forms

class CreateInForum(ModelForm):
    class Meta:
        model = forum
        fields = "__all__"



class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
