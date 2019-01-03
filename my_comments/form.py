from django import forms
from django.forms import widgets
class CommentForm(forms.Form):
    comment=forms.CharField(label='在此评论',max_length=10000,required=True, widget=forms.Textarea(attrs={'style': 'width:400px; height:100px'}))

