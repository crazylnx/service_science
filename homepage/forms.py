from django import forms
class SearchForm(forms.Form):
    KeyWord = forms.CharField(label='keyword', max_length=20)
