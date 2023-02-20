from typing import List, Dict

from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from notes.models import Notes


# new
class AllNotesView(ListView):
    model = Notes
    context_object_name = 'notes'

    # Extra
    all_notes_t = Notes.objects.values('title')
    extra_context = {'all_notes': all_notes_t}

    template_name = 'notes/notes.html'


class NoteView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note.html'


# init
def all_notes(request):
    all_notes: List[Notes] = Notes.objects.all()
    # all_notes_t = [t.title for t in all_notes]
    # in Jinja2 {{ mydict[key] }} in DTL custom template filter for new DJ version just .title
    all_notes_t: List[Dict] = Notes.objects.values('title', 'text')
    return render(request, 'notes/notes.html', {'all_notes': all_notes, 'all_notes_t': all_notes_t})


def note(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
        return render(request, 'notes/note.html', {'note': note})
    except Notes.DoesNotExist as err:
        raise Http404(err)