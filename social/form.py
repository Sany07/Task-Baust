from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import Blogpost

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



# class CreatePostForm(forms.ModelForm):

#     class Meta:

#         model=Blogpost

#         fields =[
#             'title',
#             'post',
#             'image',
#             'catagories',
#             'previous_post',
#             'next_post',



#         ]