
from django.conf.urls import url
from posts import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^post/(?P<id>\d+)$', views.post_detail, name='post_detail'),
    url(r'^postform', views.post_form, name='post_form'),
    url(r'^(?P<id>[\d+]+)/like/$', views.PostLikeToggle.as_view(), name='like-toggle'),
    url(r'^api/(?P<id>[\d+]+)/like/$', views.PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/sing_up/$', views.sing_up, name='sing_up'),
    url(r'^confirm/(?P<confirmation_code>\w+)/(?P<username>\w+)/$', views.confirm, name='confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)