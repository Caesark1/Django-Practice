from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Contacts

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contacts
        fields = ("email","captcha")
        widgets = {
            "email": forms.TextInput(attrs = {"class": "editContent", "placeholder": "Enter Your Email..."})
        } 
        labels = {
            "email": ""
        }