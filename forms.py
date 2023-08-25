import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms
#models
from .models import *

class EnergyProjectForm(forms.ModelForm):
    class Meta:
        model=EnergyProject
        fields=['end_year','intensity', 'sector','topic','insight','url','region','start_year','impact','added',
                'published','country','relevance','pestle','source','title','likelihood']