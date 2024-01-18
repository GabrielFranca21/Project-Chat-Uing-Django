from django import forms
from .models import User, Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sender'] = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
