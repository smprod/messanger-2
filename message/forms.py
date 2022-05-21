from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ("message",)

        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Текст'})
        }

    
