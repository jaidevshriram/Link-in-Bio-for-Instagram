from django import forms

class UploadFileForm(forms.Field):
    title = forms.CharField()
    img = forms.ImageField()
