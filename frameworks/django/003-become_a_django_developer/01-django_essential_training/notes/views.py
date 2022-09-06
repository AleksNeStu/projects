from django.http import Http404
from django.shortcuts import render

from .models import Notes


# Create your views here.

def all_notes(request):
    all_notes = Notes.objects.all()
    # all_notes_t = [t.title for t in all_notes]
    all_notes_t = Notes.objects.values('title')
    return render(request, 'notes/notes.html', {'notes': all_notes, 'all_notes': all_notes_t})


def note(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
        return render(request, 'notes/note.html', {'note': note})
    except Notes.DoesNotExist as err:
        raise Http404(err)