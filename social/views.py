from django.shortcuts import render , get_object_or_404
from .models import CandidateProfile
# Create your views here.


def home(request):
    

    return render(request,'index.html')


def profile(requesr,id):

    user = get_object_or_404(CandidateProfile , id=id)

    context={
        'user' :user
    }
    return render(request,'index.html' , context)


