from django import forms
class MyForms(forms.Form):
   weight=forms.CharField(label="Weight",max_length=100)
   height=forms.CharField(label="Height",max_length=100)