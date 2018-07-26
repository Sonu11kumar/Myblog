from django import forms
from .models import Post, Postman


class PostForm (forms.ModelForm):
    class Meta:
        model = Postman
        fields = ["title", "image", "description", "slug", "publish" ]


class JoinForm(forms.Form):  # or forms.ModelForm
    email = forms.EmailField()
    name = forms.CharField(max_length=120)
