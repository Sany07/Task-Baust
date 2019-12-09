from django.urls import path
from . import views


urlpatterns = [
      path('', views.Home , name='home'),
      path('cv/', views.userCv , name='cv'),
      path('registration/', views.candidateRegistration , name='candidateregister'),
      path('login/', views.logIn , name='login'),
      path('logout/', views.logOut , name='logout'),
      # path('profile/<int:id>/', views.userProfile , name='post'),

]
