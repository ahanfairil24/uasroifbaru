from django import forms

class mamaform(forms.Form):
    kitab = forms.CharField(max_length=50)
    bab = forms.CharField(max_length=40)
    fasol = forms.CharField(widget=forms.Textarea)
    penjelasan = forms.BooleanField()
