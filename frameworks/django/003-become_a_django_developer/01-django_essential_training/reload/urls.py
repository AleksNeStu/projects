from django.urls import include
from django.urls import path

from reload import views

urlpatterns = [
    path("django/", views.index_django),
    path("jinja/", views.index_jinja),
    path("favicon.ico", views.favicon),
    path("__reload__/", include("django_browser_reload.urls")),  # reload open pages
]
