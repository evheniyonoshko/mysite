
from django.conf.urls import url
from django.contrib import admin
from posts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^singin$', views.singin, name='singin'),
]
