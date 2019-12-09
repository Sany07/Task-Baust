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
    Profile_Pic = models.ImageField(upload_to='Recruter')

    def __str__(self):
        return self.user_name

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class CandidateProfile(models.Model):
    candidate =  models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_category = models.ForeignKey(Category,related_name='CandidateRegistration' , on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pics' , blank=True , null= True)
    education = models.TextField()
    personal_info = models.TextField()
    cv = models.FileField(upload_to='pdf' ,blank=True , null= True)
    website = models.URLField(blank=True , null= True)

    def __str__(self):
        return self.candidate.username


    