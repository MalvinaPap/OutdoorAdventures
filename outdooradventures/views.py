from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from django.views.decorators.csrf import csrf_protect


def index(request):
    template = loader.get_template('outdooradventures/index.html')
    return HttpResponse(template.render({},request))

@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('user exists')
            print(request.session.items())
        else:
            print('user does not exist')
            print(request.session.items())

    return redirect()


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        print(username,email, password, name, surname)

        try:
            user=  User.objects.create_user(username, email=email, password=password, first_name=name, last_name=surname)
            user.save()
            auth_login(request, user)
            print(request.session.items())
        except Exception as e:
            print(e)

    return redirect('/')



def logout(request):
    auth_logout(request)
    template = loader.get_template('outdooradventures/index.html')
    return HttpResponse(template.render({},request))
    print(request.session.items())


def activities(request):
    print(request.session.items())
    template = loader.get_template('outdooradventures/activities.html')
    return HttpResponse(template.render({},request))



def createpost(request):
    template = loader.get_template('outdooradventures/createpost.html')
    return HttpResponse(template.render({},request))


"""for future use

def userprofile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'outdooradventures/...', {'user': user})

def clubprofile(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'outdooradventures/...', {'club': club})

def activities(request):
    activities = Activity.objects.values('name')
    return render(request, 'outdooradventures/...', {'activities': activities})

def destinations(request):
    destinations = Adress.objects.values('city').distinct()
    return render(request, 'outdooradventures/...', {'destinations': destinations})

def userdashboard(request, user_id):
    return render(request, 'outdooradventures/...')

def clubdashboard(request, user_id):
    return render(request, 'outdooradventures/...')


"""
