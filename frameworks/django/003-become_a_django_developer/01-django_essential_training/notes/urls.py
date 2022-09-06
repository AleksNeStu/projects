from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.all_notes),
    path('notes/<int:pk>', views.note),
]