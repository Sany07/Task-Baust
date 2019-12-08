from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RecruterRegistration(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    user_name = models.CharField()
    email = models.CharField()
    password = models.CharField()
    confirm_pass = models.CharField()
    company_name = models.CharField()
    company_url = models.URLField()
    Profile_Pic = models.ImageField()

    def __str__(self):
        return self.user_name


class CandidateRegistration(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    candidate_user_name = models.CharField()
    email = models.CharField()
    password = models.CharField()
    confirm_pass = models.CharField()
    picture_user = models.ImageField()

    def __str__(self):
        return self.candidate_user_name


class Category(models.Model):
    category_name = models.CharField()

    def __str__(self):
        return self.category_id


class CandidateProfile(models.Model):
    candidate_pro_id = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)
    candidate_category_id = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)
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
