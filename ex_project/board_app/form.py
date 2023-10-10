from django import forms

class DataForm(forms.Form):
    title = forms.CharField(max_length=100,
                           label='title2')
    
    body = forms.CharField(max_length=5000, label='body2')