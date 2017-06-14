import random
import string
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.utils import timezone
from django.db.models import Q
from django.views.generic import RedirectView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from datetime import datetime, timedelta
from posts import forms, models

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


@login_required(login_url="accounts/login/")
def post_form(request):
    """
    Posts

    :param request: django.http.request.HttpRequest
    :return: django.http.response.HttpResponse or django.http.response.HttpResponseRedirect
    """
    context = models.Post.objects.all()
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = models.Post.objects.create(user=request.user,
                                              title=form.cleaned_data['title'],
                                              description=form.cleaned_data['description'],
                                              image=request.FILES['image'])
            post.save()
            return redirect('/')
    return render(request, 'post_form.html', context={'form': form,
                                             'context': context})


@login_required(login_url="accounts/login/")
def post_list(request):
    today = timezone.now().date()
    queryset_list = models.Post.objects.all()
    
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)|
                Q(user__country__icontains=query) |
                Q(user__city__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    
    context = {
        "object_list": queryset, 
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "post_list.html", context)


@login_required(login_url="accounts/login/")
def comment_remove(request, id):
    comment = get_object_or_404(models.Comment, id=id)
    comment.delete()
    return redirect('post_detail', id=comment.post.id)


@login_required(login_url="accounts/login/")
def add_comment_to_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment.objects.create(author=request.user,
                                                    post=post,
                                                    text=form.cleaned_data['text'])
            comment.save()
            return redirect('posts:post_detail', id=post.id)
    else:
        form = forms.CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required(login_url="accounts/login/")
def post_detail(request, id):
    instance = get_object_or_404(models.Post, id=id)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    paginator = Paginator(instance.comments.all(), 3) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)
    initial_data = {
            "content_type": instance.get_content_type,
            "object_id": instance.id
    }
    
    context = {
        "title": instance.title,
        "description": instance.description,
        "image": instance.image,
        "instance": instance,
        "comments": comments,
        "page_request_var": page_request_var,
    }
    return render(request, "post_detail.html", context)


@login_required(login_url="accounts/login/")
def post_like(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    obj = models.Post.objects.get(id=int(post_id))
    url_ = obj.get_like_url()
    user = request.user
    if user.is_authenticated():
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
    return redirect('/')


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
    return redirect('posts:list')


def send_email(request, user):
    msg = EmailMessage("Account confirmation",
                       "http://mysite-test-task.herokuapp.com/confirm/" + str(user.confirmation_code) + "/" + user.email,
                       to=[user.email])
    msg.send()
    return HttpResponseRedirect('/')


def send_registration_confirmation(request, user):
	send_email(request, user)


def confirm(request, confirmation_code, email):
    user = models.User.objects.get(email=email)
    try:
		if user.confirmation_code == confirmation_code:
			user.is_active = True
			user.save()
		return redirect('posts:list')
    except:
        user.delete()
        raise ValueError('Confirmation_code: {}, Email: {}'.format(confirmation_code, email))


def sing_up(request, page='sing_up'):
    form = forms.SingUpForm()
    if request.method == 'POST':
        form = forms.SingUpForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            try:
                user = models.User.objects.get(email=form.cleaned_data['email'])
                raise ValueError('This email address already exists. Please try again')
            except:
                confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
                user = models.User.objects.create_user(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    birthday=form.cleaned_data['birthday'],
                    country=form.cleaned_data['country'],
                    city=form.cleaned_data['city'],
                    confirmation_code=confirmation_code)
                send_registration_confirmation(request, user)
                return render(request, 'login.html', context={'form': form,
                                                              'message': 'Please confirm your email and then you can login'})
    return render(request, 'sing_up.html', context={'form': form})


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get("id")
        print(id)
        obj = get_object_or_404(models.Post, id=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id, format=None):
        # id = self.kwargs.get("id")
        obj = get_object_or_404(models.Post, id=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)
