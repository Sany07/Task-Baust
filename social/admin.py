from django.contrib import admin
from .models import  Category, CandidateProfile , RecruiterProfile , Blogpost , Ratings 

# Register your models here.

admin.site.register(RecruiterProfile)
admin.site.register(CandidateProfile)
admin.site.register(Category)
admin.site.register(Blogpost)
admin.site.register(Ratings)
# admin.site.register(Skills)