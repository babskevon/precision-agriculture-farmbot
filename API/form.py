from django import forms
from API.models import FileUpdate

class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpdate
        fields = "__all__"