from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index_django(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        # Full path due to settings.TEMPLATES BE django.template.backends.django.DjangoTemplates has DIRS=[]
        "reload/django/django.html",
        {
            "title": "It's Django templates version",
        },
    )


@require_GET
def index_jinja(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        # Not full path due to settings.TEMPLATES BE django.template.backends.django.DjangoTemplates has DIRS=[
        # **exact path to find]
        "jinja.html",
        {
            "title": "It's Jinja templates version",
        },
        using="jinja2",
    )


@require_GET
def favicon(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">🔁</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )
