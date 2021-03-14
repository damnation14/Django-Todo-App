from django import forms
from .models import activity

class ActivityForm(forms.ModelForm):

    title=forms.CharField(max_length=50)
    content=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=activity
        fields = ['title', 'content']
    
    #your_name = forms.CharField(label='Your name', max_length=100)