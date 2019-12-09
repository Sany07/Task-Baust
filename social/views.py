from django.shortcuts import render,get_object_or_404,redirect
from .models import CandidateProfile
from .form import candidateRegistrationForm
from django.contrib import auth


# Create your views here.


def Home(request):
    

    return render(request,'index.html')


def userProfile(requesr,id):

    user = get_object_or_404(CandidateProfile , id=id)

    context={
        'user' :user
    }
    return render(request,'index.html' , context)




###################### Register ##################


def candidateRegistration(request):

    form=candidateRegistrationForm(request.POST or None)

    if form.is_valid():
        form.save()

    context={
            'form':form
        }
    return render(request,'candidateregistration.html',context)




###########                                                   ########### 
#                                Login                                  #   
###########                                                   ###########


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


def logOut(request):

    auth.logout(request)
    return redirect('login')
