from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path("user_profile/<user_id>", views.user_profile, name='user_profile'),
    path('update-profile/', views.update_profile, name ='update_profile'),
    path('about_us/', views.about_us, name='about_us'),
]