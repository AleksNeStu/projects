from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthView(LoginRequiredMixin, TemplateView):
    template_name = 'home/auth.html'
    extra_context = {}
    login_url = '/admin'


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