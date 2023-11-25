from .models import todo
from django import forms

class newform(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['name','priority','date']