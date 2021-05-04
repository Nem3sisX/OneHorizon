from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("business", views.business),
    path("travel", views.travel),
    path("natural", views.natural),
    path("summary", views.summary),
]
