from django import forms
from . import models

class ComixForm(forms.ModelForm):
    class Meta:
        model = models.Manga_shops
        fields = "__all__"