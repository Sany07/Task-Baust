from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import CandidateProfile , Blogpost , RecruiterProfile

class candidateRegistrationForm(UserCreationForm):

    
    #Recruiter = forms.BooleanField()
    class Meta:

        model=User

        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            #'Recruiter'
        ]

class RecruiterProfileForm(forms.ModelForm):

    class Meta:

        model=RecruiterProfile

        fields =[
            
            'company_pic',
            'company_name',
            'website',

        ]

class CreateCvForm(forms.ModelForm):

    class Meta:

        model=CandidateProfile

        fields =[
            
            'candidate_category',
            'education',
            'personal_info',
            'website',
            'skills',
            # 'tech_skill',
            'cv',
            'profile_pic',

        ]

class userBlogPost(forms.ModelForm):

    class Meta:

        model=Blogpost

        fields =[
            
            'title',
            'post',
            'image',
            'website',
           
   

        ]

