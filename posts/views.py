import random
import string
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from datetime import datetime, timedelta
from posts import forms, models


@login_required(login_url="accounts/login/")
def index(request):
    return render(request,"base.html")

def login(request, page='login'):
    """
    Logs User in

    :param request: django.http.request.HttpRequest
    :return: django.http.response.HttpResponse or django.http.response.HttpResponseRedirect
    """
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            user = auth.authenticate(email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password'])
            if user:
                if user.is_authenticated():
                    auth.login(request, user)
                    return redirect('/')
    return render(request, 'login.html', context={'form': form})


@login_required
def logout(request):
    """
    Logs User out and redirect to Index page

    :param request: django http.request.HttpRequest
    :return: django.http.response.HttpResponseRedirect
    """
    if request.user.is_authenticated():
        auth.logout(request)
    return redirect('index')


def send_registration_confirmation(user):
	title = "Account confirmation"
	content = "http://secure-harbor-61874.herokuapp.com/confirm/" + str(user.confirmation_code) + "/" + user.email
	send_mail(title, content, 'no-reply@secure-harbor-61874.herokuapp.com', [user.email], fail_silently=False)


def confirm(request, confirmation_code, email):
	try:
		user = models.User.objects.get(email=email)
		if user.confirmation_code == confirmation_code and user.date_joined > (datetime.now()-timedelta(days=1)):
			user.is_active = True
			user.save()
			user.backend='django.contrib.auth.backends.ModelBackend' 
			auth.login(request, user)
		return redirect('index')
	except:
		return redirect('index')


def sing_up(request, page='sing_up'):
    form = forms.SingUpFrom()
    if request.method == 'POST':
        form = forms.SingUpFrom(request.POST)
        if form.is_valid():
            print(form.changed_data)
            try:
                user = models.User.objects.get(email=form.cleaned_data['email'])
                raise ValueError('This email address already exists. Please try again')
            except:
                confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
                user = models.User(email=form.cleaned_data['email'],
                                   username=form.cleaned_data['username'],
                                   first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   birthday=form.cleaned_data['birthday'],
                                   country=form.cleaned_data['country'],
                                   city=form.cleaned_data['city'],
                                   confirmation_code=confirmation_code)
                user.set_password = form.cleaned_data['password']
                user.save()
                send_registration_confirmation(user)
    return render(request, 'sing_up.html', context={'form': form})
