from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

WELCOME_T = 'home/welcome.html'
AUTH_T = 'home/authorized.html'
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
    fmt = "%d/%m/%Y %H:%M:%S:%f"
    dt1 = datetime.utcnow()
    dt_str = dt1.strftime(fmt)
    dt2 = datetime.strptime(dt_str, fmt)
    assert dt1 == dt2
    context = {'today': dt_str}
    #context = {'today': dt2}

    return render(request, WELCOME_T, context)


# to be redirected to admin (login) page is required to delete 'sessionid' cookie or make logout via UI
@login_required(login_url=ADMIN_URL)
def authv1(request):
    return render(request, AUTH_T, {})