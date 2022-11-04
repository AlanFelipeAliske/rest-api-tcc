
from unicodedata import name
from django.urls import re_path as url
from core import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),

    #url(r'^api/v1/posts$', views.posts_list),
    #url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.posts_detail),
    #url(r'^api/v2/posts$', views.PostsViewSet.as_view({'get': 'list'}), name='teste'),

    url(r'^api/v1/posts$', views.PostLists.as_view(), name='api-posts'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.PostDetail.as_view(), name='api-posts'),


    url(r'', RedirectView.as_view(url='/admin/')),
]
