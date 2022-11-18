
from unicodedata import name
from django.urls import re_path as url
from core import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/submit', views.submit_login),

    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user, name='logout_user'),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('relatorio/', views.relatorio, name='relatorio'),


    # Restframework
    url(r'^api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^api/v1/posts$', views.PostLists.as_view(), name='api-posts'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.PostDetail.as_view(), name='api-posts'),

    url(r'^api/v1/perguntas$', views.PerguntasLists.as_view(), name='api-perguntas'),
    url(r'^api/v1/perguntas/(?P<pk>[0-9]+)$', views.PerguntasDetail.as_view(), name='api-perguntas'),

    url(r'^api/v1/respostas$', views.RespostasLists.as_view(), name='api-respostas'),
    url(r'^api/v1/respostas/(?P<pk>[0-9]+)$', views.RespostasDetail.as_view(), name='api-respostas'),

    path('', RedirectView.as_view(url='/login/')),
]
