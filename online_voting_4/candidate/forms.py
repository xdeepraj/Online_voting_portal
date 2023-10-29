from django import forms
from django.forms import ModelForm
from . models import Candidate

#Create a new voter
class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        # fields = "__all__"
        fields = ('first_name', 'last_name', 'email', 'mobile_no', 'description', 'candidate_image', 'positions')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'mobile_no': '',
            'candidate_image': '',
            'description': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First name of candidate'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Second name of candidate'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email address of candidate'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number of candidate'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter candidate\'s bio'}),
        }

    