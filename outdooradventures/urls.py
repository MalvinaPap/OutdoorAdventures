from django.urls import path
import datetime
from django.utils import timezone

from . import views

app_name = 'outdooradventures'

urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.activities, name='activities'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('createpost/', views.createpost, name='createpost'),
]


"""
path('destinations', views.destinations, name='destinations'),
path('userprofile/<int:user_id>/', views.userprofile, name='userprofile'),
path('clubprofile/<int:club_id>/', views.clubprofile, name='clubprofile'),
path('userdashboard/<int:user_id>/', views.userdashboard, name='userdashboard'),
path('clubdashboard/<int:club_id>/', views.clubdashboard, name='clubdashboard'),

"""
