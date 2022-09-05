from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    # Django uses template frm to render it
    # from django.http import HttpResponse
    # return HttpResponse('Home response')

    # {} info from view to template
    return render(request, 'home/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def auth(request):
    return render(request, 'home/auth.html', {})