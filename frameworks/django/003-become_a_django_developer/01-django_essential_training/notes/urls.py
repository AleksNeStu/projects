from django.urls import path

from notes import views

# Not using / for not root path params
# /notes/...
urlpatterns = [
    # via functions
    path('notesv1', views.all_notes),
    path('notesv1/<int:pk>', views.note),

    # via views
    path('notesv2', views.AllNotesView.as_view()),
    path('notesv2/<int:pk>', views.NoteView.as_view()),
]