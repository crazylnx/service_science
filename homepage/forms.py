from django import forms
class SearchForm(forms.Form):
    KeyWord = forms.CharField( max_length=20)
