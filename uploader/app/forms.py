
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
