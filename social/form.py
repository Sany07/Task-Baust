from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import CandidateProfile

class candidateRegistrationForm(UserCreationForm):

    class Meta:

        model=User

        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]



class CreateCvForm(forms.ModelForm):

    class Meta:

        model=CandidateProfile

        fields =[
            'candidate_category',
            'education',
            'personal_info',
            'profile_pic',
 



        ]


