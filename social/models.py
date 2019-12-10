from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Candidate_profile type  CSE , EEE etc ...
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Skills(models.Model):
    skills = TaggableManager()



class CandidateProfile(models.Model):
    candidate = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_category = models.ManyToManyField(Category)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    education = models.TextField()
    personal_info = models.TextField()
    tech_skill = models.ManyToManyField(Skills)
    cv = models.FileField(upload_to='pdf', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.candidate.username


class RecruiterProfile(models.Model):
    recruiter = models.OneToOneField(User, on_delete=models.CASCADE)
    # candidate_category = models.ForeignKey(Category, related_name='CandidateRegistration', on_delete=models.CASCADE)
    company_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company_name = models.TextField()

    def __str__(self):
        return self.recruiter.username


class Blogpost(models.Model):
    author = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(blank=True, null=True)
    # videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    image = models.ImageField(upload_to='blog_image')
    # featured = models.BooleanField(default=False)
    # comment_count = models.IntegerField(default=0)
    # catagories = models.ManyToManyField(Catagory)
    website = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ratings(models.Model):
    candidate = models.ForeignKey(CandidateProfile, related_name='CandidateId', on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, related_name='BlogpostId', on_delete=models.CASCADE)
    rate = models.IntegerField()


def __str__(self):
    return self.rate

#
# class RecruterRegistration(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     user_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     confirm_pass = models.CharField(max_length=200)
#     company_name = models.CharField(max_length=200)
#     company_url = models.URLField(max_length=200)
#     Profile_Pic = models.ImageField()
#
#     def __str__(self):
#         return self.user_name
#
#
# class CandidateRegistration(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     candidate_user_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     confirm_pass = models.CharField(max_length=200)
#     picture_user = models.ImageField(max_length=200)
#
#     def __str__(self):
#         return self.candidate_user_name
#
#
# class Category(models.Model):
#     category_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.category_name
#
#
# class CandidateProfile(models.Model):
#     # candidate_id=models.IntegerField()
#     # candidate = models.OneToOneField(User, on_delete=models.CASCADE)
#     # candidate_category_id = models.ForeignKey(Category, related_name='CandidateRegistration', on_delete=models.CASCADE)
#     objective = models.TextField()
#     education = models.TextField()
#     personal_info = models.TextField()
#     projects = models.TextField()
#     technical_skill = models.TextField()
#     language = models.TextField()
#     awards = models.TextField()
#     membership = models.TextField()
#     interest = models.TextField()
#     hobbies = models.TextField()
#     personal_qualities = models.TextField()
#
#     def __str__(self):
#         return self.candidate_category_id
#
#
# class Post(models.Model):
#     recruiter_post = models.CharField(max_length=400)
#     recruiter_vid = models.URLField()
#     recruiter_Img = models.IntegerField()
#     post_rating = models.IntegerField()
#     post_comment = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.recruiter_post
