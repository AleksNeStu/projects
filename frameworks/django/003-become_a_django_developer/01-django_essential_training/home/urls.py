from django.urls import path

from . import views as home_views

urlpatterns = [
    # path('home/', home_views.home),
    # path('auth/', home_views.auth),
    path('home/', home_views.HomeView.as_view()),
    path('auth/', home_views.AuthView.as_view()),
]