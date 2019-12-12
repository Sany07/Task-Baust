from django.shortcuts import render,get_object_or_404,redirect
from .models import CandidateProfile ,  RecruiterProfile , Blogpost 
from .form import candidateRegistrationForm , CreateCvForm , userBlogPost , RecruiterProfileForm 
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from taggit.models import Tag
from django.db.models import Q
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
User=get_user_model()

###################### Search #####################


def search(request):

    search_profile_list=CandidateProfile.objects.all()
    query= request.GET.get('text')
    print(query)

    if query:
        search_profile_list= search_profile_list.filter(
            Q(skills__slug__icontains=query) |
            Q(education__icontains=query)|
            Q(website__icontains=query)
        ).distinct()
        print('query')
        print(search_profile_list)

    context={

        'profile_list':search_profile_list,
        'query':query,
    }
    return render(request,'result.html',context)

###################### Home #####################

def home(request):
    
    post_list=Blogpost.objects.order_by('-timestamp')


    context={
        'post_list' : post_list,
    }
    if request.user.is_authenticated:
        user = get_object_or_404(User , id=request.user.id)
        recruiter_profile = RecruiterProfile.objects.filter(recruiter=user.id)
        candidate_profile = CandidateProfile.objects.filter(candidate=user.id)

        context={
                    'post_list':post_list,
                    'recruiter_profile':recruiter_profile,
                    'candidate_profile':candidate_profile,

                }
      
        return render(request , 'index.html',context)

    return render(request , 'index.html',context)


###################### Register ##################


def registration(request):

    form=candidateRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('login')

    context={
        
            'form':form
        }
    return render(request,'register.html',context)


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

###################### Select ###################
@login_required
def select(request):
    return render(request,'select.html')
###################### RecuiterCv ###################

@login_required
def recruterProfile(request):
    
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

@login_required
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
                return redirect ('home')
            else:
                messages.error(request,form.errors)
            context={
                'form':form
            }  
            return render(request,'cv.html',context)

###################### userCv ###################
@login_required


def blogPost(request):
    
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
                return redirect ('home')
            else:
                messages.error(request,form.errors)
            context={
                    'form':form
                }  
            return render(request,'blogpost.html',context)


# ###################### Post ###################

# def post(request,id):
    
    
#     post_list=get_object_or_404(Blogpost,pk=id)
#     latest_post_list=Blogpost.objects.order_by('-timestamp')[0:3]
 
    
#     context={
#         'post' :post_list,
#         'latest_post_list':latest_post_list,
       
#     }
#     return render(request , 'post.html',context)

###################### Profile ###################

def userprofile(request,id):
   
    profile = get_object_or_404(CandidateProfile , id=id)

    
    context={
        'profile': profile,
 
    }

    return render(request,'profile.html',context)


###################### Job single Post ###################

def singlePost(request,id):
    
    post_list=get_object_or_404(Blogpost,pk=id)
    

    context={
        'post' :post_list,

    }
    return render(request , 'singlepost.html',context)


###################### Job Post Likes ###################

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("id")
        print(slug)
        obj = get_object_or_404(Blogpost, id=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_




# def category(request , name):
  
#     latest_post_list=Blogpost.objects.order_by('-timestamp')[0:3]
#     cat = get_object_or_404(Catagory , title=name)
#     category_count=get_category_count()
#     post = Blogpost.objects.filter(catagories=cat.id)

#     context={
#         'post_list': post,
#         'latest_post_list':latest_post_list,
#         'category_count':category_count
#     }

#     return render(request ,'category.html',context)


################# __Edit Post__


# @login_required
# def updatepost(request,id):
#     if request.user.is_authenticated:
#         user=get_object_or_404(Author,user=request.user.id)
#         post=get_object_or_404(Blogpost,id=id)
#     form=CreatePostForm(request.POST or None , request.FILES or None , instance=post)
    
#     if request.method=='POST':
#         if form.is_valid():
#             instance=form.save(commit=False)
#             instance.author=user
#             instance.save()
           
#             return redirect(reverse("post" ,kwargs={
#                 'id':form.instance.id
#         }))
#     context={
#         'form':form
#     }
#     return render(request,'create_post.html',context)


###########_post_delete


# @login_required
# def delete(request,id):
#     post=get_object_or_404(Blogpost,id=id)
#     user=get_object_or_404(Author,user=request.user.id)
    
#     if user:
    
#         post.delete()

#     return redirect('blog')



# def search(request):

#     search_post_list=Blogpost.objects.all()
#     query= request.GET.get('text')
#     if query:
#         search_post_list= search_post_list.filter(
#             Q(title__icontains=query) |
#             Q(post__icontains=query)
#         ).distinct()
#         print(search_post_list)
#     context={

#         'post_list':search_post_list,
        
#     }
#     return render(request,'result.html',context)

