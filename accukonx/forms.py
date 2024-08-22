from django import forms

class CreateNewPersons(forms.Form):
    name =forms.CharField(label="Name",max_length=200)
    age =forms.IntegerField(label="age")
    check = forms.BooleanField(required=False)

class UploadFileForm(forms.Form):
    file =forms.FileField(label ="upload file")