
from django.conf.urls import url
from django.contrib import admin, auth
from posts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/sing_up/$', views.sing_up, name='sing_up'),
    url(r'^confirm/(?P<confirmation_code>\w+)/(?P<username>\w+)/$', views.confirm, name='confirm'),
]
