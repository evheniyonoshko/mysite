
from django.conf.urls import url
from posts import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)$', views.post, name='post_detail'),
    url(r'^post/(?P<post_id>\d+)/like/$', views.post_like, name='post_like'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/sing_up/$', views.sing_up, name='sing_up'),
    url(r'^confirm/(?P<confirmation_code>\w+)/(?P<username>\w+)/$', views.confirm, name='confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)