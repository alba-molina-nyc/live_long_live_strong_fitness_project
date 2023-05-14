from django import forms
from .models import FitnessBlogComment, ContactUs, Testimonial

class CommentForm(forms.ModelForm):
    class Meta:
        model = FitnessBlogComment
        fields = ('name', 'email', 'comment_body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter your comment'}),
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('name', 'job_title', 'age', 'quote', 'image',)
        widgets = {
            'quote': forms.Textarea(attrs={'rows': 3}),
        }
