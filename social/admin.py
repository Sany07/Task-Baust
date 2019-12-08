from django.contrib import admin
from social.models import RecruterRegistration, CandidateRegistration, Category, CandidateProfile

admin.site.register(RecruterRegistration)
admin.site.register(CandidateRegistration)
admin.site.register(CandidateProfile)
admin.site.register(Category)
