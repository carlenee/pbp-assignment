from django import forms

from .models import *

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'size':'30'}))
    description= forms.CharField(widget=forms.Textarea(attrs={'size': '60'}))

    class Meta:
        model = Task
        fields = ('title', 'description')