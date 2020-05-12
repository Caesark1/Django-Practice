from .models import Comment,Movie
from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class CommentAddForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ["name", "email", "text", "captcha"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border","id": "contactcomment"})
        }

