from django import forms
from .models import FitnessBlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = FitnessBlogComment
        fields = ('name', 'email', 'comment_body', 'parent_comment')
        widgets = {
            'parent_comment': forms.HiddenInput()
        }
