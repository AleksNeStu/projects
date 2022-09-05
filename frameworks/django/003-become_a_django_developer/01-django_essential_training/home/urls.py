from django.urls import path

from . import views as home_views

urlpatterns = [
    path('home/', home_views.home),
    path('auth/', home_views.auth),
]