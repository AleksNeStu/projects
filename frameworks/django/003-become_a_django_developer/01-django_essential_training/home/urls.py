from django.urls import path

from home import views

urlpatterns = [
    # path('home/', home_views.home),
    # /homev1 -> smartnotes/urls.py -> home/urls.py -> home/views.py -> def homev1
    path('homev1/', views.homev1),
    path('homev2/', views.homev2),
    # path('auth/', views.auth),

    path('home/', views.HomeView.as_view()),
    path('auth/', views.AuthView.as_view()),
]