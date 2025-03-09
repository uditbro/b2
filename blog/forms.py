from django import forms
from .models import Topic,Entry,Picture

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topics']
        labels = {'topics': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entries']
        labels = {'entries': ''}
        widgets = {'entries': forms.Textarea(attrs={'cols':100})}

