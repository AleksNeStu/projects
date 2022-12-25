# Create your views here.
from django.views.generic import View


class ReportErrorView(View):

    def get(self, request, *args, **kwargs):
        return 1 / 0
