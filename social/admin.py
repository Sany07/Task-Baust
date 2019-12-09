from django.contrib import admin
from .models import RecruterRegistration , Category, CandidateProfile

# Register your models here.



admin.site.register(RecruterRegistration)
# admin.site.register(CandidateRegistration)
admin.site.register(CandidateProfile)
admin.site.register(Category)
