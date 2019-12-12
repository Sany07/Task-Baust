from django.urls import path,include
from . import views


urlpatterns = [
        path('', views.home , name='home'),
        path('cv/', views.userCv , name='cv'),
        path('r/', views.recruterProfile , name='recruterprofile'),
        path('post/', views.blogPost , name='post'),
        path('register/', views.registration , name='register'),
        path('login/', views.logIn , name='login'),
        path('logout/', views.logOut , name='logout'),
        path('select/', views.select , name='select'),
        path('profile/<int:id>/', views.userprofile , name='profile'),
        path('singlepost/<int:id>/', views.singlePost , name='singlepost'),
        path('result/', views.search , name='result'),
        path('singlepost/<int:id>/like/', views.PostLikeToggle.as_view(), name='like_toggle'),


     
        

]
