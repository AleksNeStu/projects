from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Django uses template frm to render it
    # return HttpResponse('Home response')

    # {} info from view to template
    return render(request, 'home/welcome.html', {'today': datetime.today()})