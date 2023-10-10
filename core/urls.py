"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.web.views import *
from apps.dashboard.views import signin

from django.conf.urls import handler404

handler404 = 'apps.web.views.custom_404'


urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    path('cientificos/', ScientistView.as_view(), name='scientist'),
    path('observatorios/', ObservatoriestView.as_view(), name='observatories'),
    path('telescopios/', TelescopesView.as_view(), name='telescopes'),
    path('news/', NewsView.as_view(), name='news' ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
   
    
    path('cientificos/<slug:slug>/', PostDetail.as_view(), name='scientist_detail' ),
    path('observatorios/<slug:slug>/', PostDetail.as_view(), name='observatory_detail' ),
    path('telescopios/<slug:slug>/', PostDetail.as_view(), name='telescope_detail' ),
    path('news/<slug:slug>/', PostDetail.as_view(), name='news_detail' ),
    
    path('signindashadpagemng/', signin, name='signin'),
    
    
    path('dashboard/', include('apps.dashboard.urls'))
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

