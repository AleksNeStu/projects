import os

import django
from django.test import Client
from html_form_to_dict import html_form_to_dict

# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "admin.settings")
django.setup()

c = Client()
response = c.get("example.com")
res_html = response.content
res_dict = html_form_to_dict(res_html)
assert response.status_code == 200

def test_foo(client):
    url = "example.com"

    # client is a DjangoClient. But you could use
    # python-requests or a different URL-lib, too
    response = client.get(url)

    # This method parses the HTML in response.content to a dictionary.
    # This dictionary is like request.POST or request.GET.
    # It is a flat mapping from the input elements of the form
    # to their value.
    data = html_form_to_dict(response.content)

    # Now you can test the default values of the form.
    assert data == {'city': 'Chemnitz', 'name': 'Mr. X'}

    # You can edit the data. This is like a human (or Playwright/Selenium)
    # altering the HTML input fields
    data['name'] = 'Mrs. Y'

    # This submits the data to the server.
    # This methods uses the "action" attribute of the form.
    # The hx-get, hx-post attributes of htmx are supported, too
    response = data.submit(client)

    # If you use the Post/Redirect/Get pattern:
    assert response.status == 302, response.context['form'].errors