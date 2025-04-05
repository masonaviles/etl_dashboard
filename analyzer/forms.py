from django import forms
from .models import UploadSession

class CSVUploadForm(forms.ModelForm):
    class Meta:
        model = UploadSession
        fields = ['file']
