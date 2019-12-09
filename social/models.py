from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User=get_user_model()
# Create your models here.

class RecruterRegistration(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_pass = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length=200)
    Profile_Pic = models.ImageField(max_length=200)

    def __str__(self):
        return self.user_name


# class CandidateRegistration(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     candidate_user_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password1 = models.CharField(max_length=200)
#     password2 = models.CharField(max_length=200)
#     picture_user = models.ImageField(max_length=200)

#     def __str__(self):
#         return self.candidate_user_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class CandidateProfile(models.Model):
    candidate =  models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_category = models.ForeignKey(Category,related_name='CandidateRegistration' , on_delete=models.CASCADE)
    objective = models.TextField()
    education = models.TextField()
    personal_info = models.TextField()
    projects = models.TextField()
    technical_skill = models.TextField()
    language = models.TextField()
    awards = models.TextField()
    membership = models.TextField()
    interest = models.TextField()
    hobbies = models.TextField()
    personal_qualities = models.TextField()

    def __str__(self):
        return self.candidate_category_id
