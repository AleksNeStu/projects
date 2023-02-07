from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

WELCOME_T = 'home/welcome.html'
AUTH_T = 'home/auth.html'
ADMIN_URL = '/admin'

# new
class HomeView(TemplateView):
    template_name = WELCOME_T
    extra_context = {'today': datetime.today()}


class AuthView(LoginRequiredMixin, TemplateView):
    template_name = AUTH_T
    extra_context = {}
    login_url = ADMIN_URL


# init
def homev1(request):
    return HttpResponse('Home response v1')

def homev2(request):
    # {} info from view to template
    context = {'today': datetime.today()}
    return render(request, WELCOME_T, context)

@login_required(login_url=ADMIN_URL)
def auth(request):
    return render(request, AUTH_T, {})