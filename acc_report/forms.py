from django import forms

class UploadFileForm(forms.Form):
    sad_file = forms.FileField(label='Upload SAD File')
    budget_file = forms.FileField(label='Upload Budget File')
    