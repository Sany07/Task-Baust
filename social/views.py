from django.shortcuts import render,get_object_or_404,redirect
from .models import CandidateProfile
from .form import candidateRegistrationForm , CreateCvForm
from django.contrib import auth
from django.contrib.auth import get_user_model
User=get_user_model()

###################### Home #####################

def Home(request):
    
    return render(request,'index.html')

###################### Register ##################


def candidateRegistration(request):

    form=candidateRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
            'form':form
        }
    return render(request,'candidateregistration.html',context)


###################### LogIn #####################


def logIn(request):

    if request.user.is_authenticated:
        return redirect('home') 
    else:
        if request.method=='POST':
            username=request.POST['user_name']
            password=request.POST['pass']
            user=auth.authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request ,user)
                return redirect('home')
    return render(request,'login.html')


###################### LogOut ###################

def logOut(request):
    auth.logout(request)
    return redirect('login')

###################### userCv ###################


def userCv(request):
    
    if request.user.is_authenticated:
        user = get_object_or_404(User , id=request.user.id)
        cv_profile = CandidateProfile.objects.filter(candidate=user.id)
        if cv_profile:
            return render(request,'profile.html')
        else:
            form=CreateCvForm(request.POST or None , request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.candidate=user
                instance.save()
            context={
                'form':form
            }  
            return render(request,'cv.html',context)


# def userProfile(requesr,id):
#     user = get_object_or_404(CandidateProfile , id=id)
#     context={
#         'user' :user
#     }
#     return render(request,'index.html' , context)