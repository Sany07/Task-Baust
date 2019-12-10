from django.shortcuts import render,get_object_or_404,redirect
from .models import CandidateProfile ,  RecruiterProfile
from .form import candidateRegistrationForm , CreateCvForm , userBlogPost , RecruiterProfileForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from taggit.models import Tag
User=get_user_model()

###################### Home #####################

def Home(request):
    
    return render(request,'index.html')

###################### Register ##################


def candidateRegistration(request):

    form=candidateRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
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


###################### RecuiterCv ###################


def RecruterProfile(request):
    
    if request.user.is_authenticated:
        user = get_object_or_404(User , id=request.user.id)
        profile = RecruiterProfile.objects.filter(recruiter=user.id)
        if profile:
            return redirect('post')
        else:
            form=RecruiterProfileForm(request.POST or None , request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.recruiter=user
                instance.save()
                
                messages.success(request, 'Job Profile created successfully.')
            else:
                messages.error(request,form.errors)
            context={
                'form':form
            }  
            return render(request,'recuiter.html',context)


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
                form.save_m2m()
                messages.success(request, 'Job Profile created successfully.')
            else:
                messages.error(request,form.errors)
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


def BlogPost(request):
    
    if request.user.is_authenticated:
        user = get_object_or_404(User , id=request.user.id)
        
        profile = RecruiterProfile.objects.filter(recruiter=user.id)

        if not profile:
            return redirect('recruterprofile')
        else:
            rr = get_object_or_404(RecruiterProfile , recruiter=request.user.id)
            form=userBlogPost(request.POST or None , request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.author=rr
                instance.save()
                    # form.save_m2m()
                messages.success(request, 'Job Profile created successfully.')
            else:
                messages.error(request,form.errors)
            context={
                    'form':form
                }  
            return render(request,'blogpost.html',context)