from django.urls import path

from home import views

# Not using / for not root path params
# /home/...
urlpatterns = [
    # via functions
    # path('home/', home_views.home),
    # /homev1 -> smartnotes/urls.py -> home/urls.py -> home/views.py -> def homev1
    path('homev1', views.homev1),
    path('homev2', views.homev2),
    path('authorizedv1', views.authv1),

    # via views
    path('homev3', views.HomeView.as_view()),
    path('authorizedv2', views.AuthView.as_view()),
]