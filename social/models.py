from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager
from django.urls import reverse
User=get_user_model()
# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

# class Skills(models.Model):
#     skills = TaggableManager()

class CandidateProfile(models.Model):
    candidate = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_category = models.ManyToManyField(Category)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    education = models.TextField()
    personal_info = models.TextField()
    # tech_skill = models.ManyToManyField(Skills)
    skills = TaggableManager()
    cv = models.FileField(upload_to='pdf', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.candidate.username

    def get_absolute_url(self):
        return reverse('profile',kwargs={

            'id':self.id
        })

class RecruiterProfile(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    company_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company_name =  models.CharField(max_length=250)

    def __str__(self):
        return self.recruiter.username
    # def get_absolute_url(self):
    #     return reverse('singlepost',kwargs={

    #         'id':self.id
    #     })

class Blogpost(models.Model):
    author = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    post = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_image')
    website = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes= models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('singlepost',kwargs={

            'id':self.id
        })
    def get_like_url(self):
        return reverse("post:like_toggle", kwargs={"id": self.id})

class Ratings(models.Model):
    candidate = models.ForeignKey(CandidateProfile, related_name='CandidateId', on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, related_name='BlogpostId', on_delete=models.CASCADE)
    rate = models.IntegerField()


    def __str__(self):

        return self.post.title


# class RecruterRegistration(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     user_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     confirm_pass = models.CharField(max_length=200)
#     company_name = models.CharField(max_length=200)
#     company_url = models.URLField(max_length=200)
#     Profile_Pic = models.ImageField(upload_to='Recruter')

#     def __str__(self):
#         return self.user_name


# class CandidateProfile(models.Model):
#     candidate =  models.OneToOneField(User, on_delete=models.CASCADE)
#     candidate_category = models.ForeignKey(Category,related_name='CandidateRegistration' , on_delete=models.CASCADE)
#     profile_pic= models.ImageField(upload_to='profile_pics' , blank=True , null= True)
#     education = models.TextField()
#     personal_info = models.TextField()
#     cv = models.FileField(upload_to='pdf' ,blank=True , null= True)
#     website = models.URLField(blank=True , null= True)

#     def __str__(self):
#         return self.candidate.username
