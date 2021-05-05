"""newsproject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from newsapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.general, name="general"),
    path("technology", views.technology, name="technology"),
    path("business", views.business, name="business"),
    path("entertain", views.entertainment, name="entertainment"),
    path("sports", views.sports, name="general"),
    path("date", views.date_fetch, name="date_fetch"),
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("register", views.register)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

