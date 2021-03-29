"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from . import views

urlpatterns = [
    # /
    path('', views.index, name='index'),
    # /login/
    path('login/', views.login_view, name='login'),
    # /logout/
    path('logout/', views.logout_view, name='logout'),
    # /post_motorcycle/
    path('post_url/', views.post_motorcycle, name='post_motorcycle'),
    # /like_motorcycle/
    path('like_motorcycle/', views.like_motorcycle, name='like_motorcycle'),
    # /id/
    re_path(r'^([0-9]+)/$', views.product_details, name='product-details'),
    # /user/username/
    re_path(r'user/(\w+)/$', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += [
        # /media/
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]
