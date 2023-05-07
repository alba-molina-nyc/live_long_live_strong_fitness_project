from django import forms
from .models import FitnessBlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = FitnessBlogComment
        fields = ('name', 'email', 'comment_body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter your comment'}),
        }
