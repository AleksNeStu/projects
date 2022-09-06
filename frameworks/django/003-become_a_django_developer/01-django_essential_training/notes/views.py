from django.shortcuts import render

# Create your views here.


from .models import Notes

def all_notes(request):
    all_notes = Notes.objects.all()
    # all_notes_t = [t.title for t in all_notes]
    all_notes_t = Notes.objects.values('title')
    return render(request, 'notes/notes.html', {'notes': all_notes, 'all_notes': all_notes_t})