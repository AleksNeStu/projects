---
source: https://docs.djangoproject.com/en/1.8/topics/testing/tools/

created: 2023-10-18T18:13:57 (UTC +02:00)

tags: [Python,Django,framework,open-source]

author: 

---
# Testing tools | Django documentation | Django
---
## Testing tools[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#testing-tools "Permalink to this headline")

Django provides a small set of tools that come in handy when writing tests.

## The test client[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#the-test-client "Permalink to this headline")

The test client is a Python class that acts as a dummy Web browser, allowing you to test your views and interact with your Django-powered application programmatically.

Some of the things you can do with the test client are:

-   Simulate GET and POST requests on a URL and observe the response – everything from low-level HTTP (result headers and status codes) to page content.
-   See the chain of redirects (if any) and check the URL and status code at each step.
-   Test that a given request is rendered by a given Django template, with a template context that contains certain values.

Note that the test client is not intended to be a replacement for [Selenium](http://seleniumhq.org/) or other “in-browser” frameworks. Django’s test client has a different focus. In short:

-   Use Django’s test client to establish that the correct template is being rendered and that the template is passed the correct context data.
-   Use in-browser frameworks like [Selenium](http://seleniumhq.org/) to test _rendered_ HTML and the _behavior_ of Web pages, namely JavaScript functionality. Django also provides special support for those frameworks; see the section on [`LiveServerTestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.LiveServerTestCase "django.test.LiveServerTestCase") for more details.

A comprehensive test suite should use a combination of both test types.

### Overview and a quick example[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#overview-and-a-quick-example "Permalink to this headline")

To use the test client, instantiate `django.test.Client` and retrieve Web pages:

```
>>> from django.test import Client
>>> c = Client()
>>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
>>> response.status_code
200
>>> response = c.get('/customer/details/')
>>> response.content
b'<!DOCTYPE html...'

```

As this example suggests, you can instantiate `Client` from within a session of the Python interactive interpreter.

Note a few important things about how the test client works:

-   The test client does _not_ require the Web server to be running. In fact, it will run just fine with no Web server running at all! That’s because it avoids the overhead of HTTP and deals directly with the Django framework. This helps make the unit tests run quickly.
    
-   When retrieving pages, remember to specify the _path_ of the URL, not the whole domain. For example, this is correct:
    
    This is incorrect:
    
    ```
    >>> c.get('http://www.example.com/login/')
    
    ```
    
    The test client is not capable of retrieving Web pages that are not powered by your Django project. If you need to retrieve other Web pages, use a Python standard library module such as [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "(in Python v3.8)").
    
-   To resolve URLs, the test client uses whatever URLconf is pointed-to by your [`ROOT_URLCONF`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-ROOT_URLCONF) setting.
    
-   Although the above example would work in the Python interactive interpreter, some of the test client’s functionality, notably the template-related functionality, is only available _while tests are running_.
    
    The reason for this is that Django’s test runner performs a bit of black magic in order to determine which template was loaded by a given view. This black magic (essentially a patching of Django’s template system in memory) only happens during test running.
    
-   By default, the test client will disable any CSRF checks performed by your site.
    
    If, for some reason, you _want_ the test client to perform CSRF checks, you can create an instance of the test client that enforces CSRF checks. To do this, pass in the `enforce_csrf_checks` argument when you construct your client:
    
    ```
    >>> from django.test import Client
    >>> csrf_client = Client(enforce_csrf_checks=True)
    
    ```
    

### Making requests[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#making-requests "Permalink to this headline")

Use the `django.test.Client` class to make requests.

_class_ `Client`(_enforce\_csrf\_checks=False_, _\*\*defaults_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client "Permalink to this definition")

It requires no arguments at time of construction. However, you can use keywords arguments to specify some default headers. For example, this will send a `User-Agent` HTTP header in each request:

```
>>> c = Client(HTTP_USER_AGENT='Mozilla/5.0')

```

The values from the `extra` keywords arguments passed to [`get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get"), [`post()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.post "django.test.Client.post"), etc. have precedence over the defaults passed to the class constructor.

The `enforce_csrf_checks` argument can be used to test CSRF protection (see above).

Once you have a `Client` instance, you can call any of the following methods:

`get`(_path_, _data=None_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.get)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "Permalink to this definition")

New in Django 1.7:

The `secure` argument was added.

Makes a GET request on the provided `path` and returns a `Response` object, which is documented below.

The key-value pairs in the `data` dictionary are used to create a GET data payload. For example:

```
>>> c = Client()
>>> c.get('/customers/details/', {'name': 'fred', 'age': 7})

```

…will result in the evaluation of a GET request equivalent to:

```
/customers/details/?name=fred&age=7

```

The `extra` keyword arguments parameter can be used to specify headers to be sent in the request. For example:

```
>>> c = Client()
>>> c.get('/customers/details/', {'name': 'fred', 'age': 7},
...       HTTP_X_REQUESTED_WITH='XMLHttpRequest')

```

…will send the HTTP header `HTTP_X_REQUESTED_WITH` to the details view, which is a good way to test code paths that use the [`django.http.HttpRequest.is_ajax()`](https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.is_ajax "django.http.HttpRequest.is_ajax") method.

CGI specification

The headers sent via `**extra` should follow [CGI](http://www.w3.org/CGI/) specification. For example, emulating a different “Host” header as sent in the HTTP request from the browser to the server should be passed as `HTTP_HOST`.

If you already have the GET arguments in URL-encoded form, you can use that encoding instead of using the data argument. For example, the previous GET request could also be posed as:

```
>>> c = Client()
>>> c.get('/customers/details/?name=fred&age=7')

```

If you provide a URL with both an encoded GET data and a data argument, the data argument will take precedence.

If you set `follow` to `True` the client will follow any redirects and a `redirect_chain` attribute will be set in the response object containing tuples of the intermediate urls and status codes.

If you had a URL `/redirect_me/` that redirected to `/next/`, that redirected to `/final/`, this is what you’d see:

```
>>> response = c.get('/redirect_me/', follow=True)
>>> response.redirect_chain
[('http://testserver/next/', 302), ('http://testserver/final/', 302)]

```

If you set `secure` to `True` the client will emulate an HTTPS request.

`post`(_path_, _data=None_, _content\_type=MULTIPART\_CONTENT_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.post)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.post "Permalink to this definition")

Makes a POST request on the provided `path` and returns a `Response` object, which is documented below.

The key-value pairs in the `data` dictionary are used to submit POST data. For example:

```
>>> c = Client()
>>> c.post('/login/', {'name': 'fred', 'passwd': 'secret'})

```

…will result in the evaluation of a POST request to this URL:

…with this POST data:

If you provide `content_type` (e.g. _text/xml_ for an XML payload), the contents of `data` will be sent as-is in the POST request, using `content_type` in the HTTP `Content-Type` header.

If you don’t provide a value for `content_type`, the values in `data` will be transmitted with a content type of _multipart/form-data_. In this case, the key-value pairs in `data` will be encoded as a multipart message and used to create the POST data payload.

To submit multiple values for a given key – for example, to specify the selections for a `<select multiple>` – provide the values as a list or tuple for the required key. For example, this value of `data` would submit three selected values for the field named `choices`:

```
{'choices': ('a', 'b', 'd')}

```

Submitting files is a special case. To POST a file, you need only provide the file field name as a key, and a file handle to the file you wish to upload as a value. For example:

```
>>> c = Client()
>>> with open('wishlist.doc') as fp:
...     c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})

```

(The name `attachment` here is not relevant; use whatever name your file-processing code expects.)

You may also provide any file-like object (e.g., [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "(in Python v3.8)") or [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "(in Python v3.8)")) as a file handle.

New in Django 1.8:

The ability to use a file-like object was added.

Note that if you wish to use the same file handle for multiple `post()` calls then you will need to manually reset the file pointer between posts. The easiest way to do this is to manually close the file after it has been provided to `post()`, as demonstrated above.

You should also ensure that the file is opened in a way that allows the data to be read. If your file contains binary data such as an image, this means you will need to open the file in `rb` (read binary) mode.

The `extra` argument acts the same as for [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

If the URL you request with a POST contains encoded parameters, these parameters will be made available in the request.GET data. For example, if you were to make the request:

```
>>> c.post('/login/?visitor=true', {'name': 'fred', 'passwd': 'secret'})

```

… the view handling this request could interrogate request.POST to retrieve the username and password, and could interrogate request.GET to determine if the user was a visitor.

If you set `follow` to `True` the client will follow any redirects and a `redirect_chain` attribute will be set in the response object containing tuples of the intermediate urls and status codes.

If you set `secure` to `True` the client will emulate an HTTPS request.

`head`(_path_, _data=None_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.head)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.head "Permalink to this definition")

Makes a HEAD request on the provided `path` and returns a `Response` object. This method works just like [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get"), including the `follow`, `secure` and `extra` arguments, except it does not return a message body.

`options`(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.options)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.options "Permalink to this definition")

Makes an OPTIONS request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.

The `follow`, `secure` and `extra` arguments act the same as for [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

`put`(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.put)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.put "Permalink to this definition")

Makes a PUT request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.

The `follow`, `secure` and `extra` arguments act the same as for [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

`patch`(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.patch)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.patch "Permalink to this definition")

Makes a PATCH request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

The `follow`, `secure` and `extra` arguments act the same as for [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

`delete`(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.delete)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.delete "Permalink to this definition")

Makes an DELETE request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.

The `follow`, `secure` and `extra` arguments act the same as for [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

`trace`(_path_, _follow=False_, _secure=False_, _\*\*extra_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.trace)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.trace "Permalink to this definition")

New in Django 1.8.

Makes a TRACE request on the provided `path` and returns a `Response` object. Useful for simulating diagnostic probes.

Unlike the other request methods, `data` is not provided as a keyword parameter in order to comply with [**RFC 2616**](https://tools.ietf.org/html/rfc2616.html), which mandates that TRACE requests should not have an entity-body.

The `follow`, `secure`, and `extra` arguments act the same as for [`Client.get()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

`login`(_\*\*credentials_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.login)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.login "Permalink to this definition")

If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/1.8/topics/auth/) and you deal with logging in users, you can use the test client’s `login()` method to simulate the effect of a user logging into the site.

Inactive users ([`is_active=False`](https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.models.User.is_active "django.contrib.auth.models.User.is_active")) are not permitted to login as this method is meant to be equivalent to the [`login()`](https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.login "django.contrib.auth.login") view which uses [`AuthenticationForm`](https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm "django.contrib.auth.forms.AuthenticationForm") and therefore defaults to rejecting users who are inactive.

After you call this method, the test client will have all the cookies and session data required to pass any login-based tests that may form part of a view.

The format of the `credentials` argument depends on which [authentication backend](https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#authentication-backends) you’re using (which is configured by your [`AUTHENTICATION_BACKENDS`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-AUTHENTICATION_BACKENDS) setting). If you’re using the standard authentication backend provided by Django (`ModelBackend`), `credentials` should be the user’s username and password, provided as keyword arguments:

```
>>> c = Client()
>>> c.login(username='fred', password='secret')

# Now you can access a view that's only available to logged-in users.

```

If you’re using a different authentication backend, this method may require different credentials. It requires whichever credentials are required by your backend’s `authenticate()` method.

`login()` returns `True` if it the credentials were accepted and login was successful.

Finally, you’ll need to remember to create user accounts before you can use this method. As we explained above, the test runner is executed using a test database, which contains no users by default. As a result, user accounts that are valid on your production site will not work under test conditions. You’ll need to create users as part of the test suite – either manually (using the Django model API) or with a test fixture. Remember that if you want your test user to have a password, you can’t set the user’s password by setting the password attribute directly – you must use the [`set_password()`](https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.models.User.set_password "django.contrib.auth.models.User.set_password") function to store a correctly hashed password. Alternatively, you can use the [`create_user()`](https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user "django.contrib.auth.models.UserManager.create_user") helper method to create a new user with a correctly hashed password.

`logout`()[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/client/#Client.logout)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.logout "Permalink to this definition")

If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/1.8/topics/auth/), the `logout()` method can be used to simulate the effect of a user logging out of your site.

After you call this method, the test client will have all the cookies and session data cleared to defaults. Subsequent requests will appear to come from an [`AnonymousUser`](https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser "django.contrib.auth.models.AnonymousUser").

### Testing responses[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#testing-responses "Permalink to this headline")

The `get()` and `post()` methods both return a `Response` object. This `Response` object is _not_ the same as the `HttpResponse` object returned by Django views; the test response object has some additional data useful for test code to verify.

Specifically, a `Response` object has the following attributes:

_class_ `Response`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response "Permalink to this definition")

`client`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.client "Permalink to this definition")

The test client that was used to make the request that resulted in the response.

`content`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.content "Permalink to this definition")

The body of the response, as a bytestring. This is the final page content as rendered by the view, or any error message.

`context`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.context "Permalink to this definition")

The template `Context` instance that was used to render the template that produced the response content.

If the rendered page used multiple templates, then `context` will be a list of `Context` objects, in the order in which they were rendered.

Regardless of the number of templates used during rendering, you can retrieve context values using the `[]` operator. For example, the context variable `name` could be retrieved using:

```
>>> response = client.get('/foo/')
>>> response.context['name']
'Arthur'

```

Not using Django templates?

This attribute is only populated when using the [`DjangoTemplates`](https://docs.djangoproject.com/en/1.8/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") backend. If you’re using another template engine, [`context_data`](https://docs.djangoproject.com/en/1.8/ref/template-response/#django.template.response.SimpleTemplateResponse.context_data "django.template.response.SimpleTemplateResponse.context_data") may be a suitable alternative on responses with that attribute.

`request`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.request "Permalink to this definition")

The request data that stimulated the response.

`wsgi_request`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.wsgi_request "Permalink to this definition")

New in Django 1.7.

The `WSGIRequest` instance generated by the test handler that generated the response.

`status_code`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.status_code "Permalink to this definition")

The HTTP status of the response, as an integer. See [**RFC 2616#section-10**](https://tools.ietf.org/html/rfc2616.html#section-10) for a full list of HTTP status codes.

`templates`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.templates "Permalink to this definition")

A list of `Template` instances used to render the final content, in the order they were rendered. For each template in the list, use `template.name` to get the template’s file name, if the template was loaded from a file. (The name is a string such as `'admin/index.html'`.)

Not using Django templates?

This attribute is only populated when using the [`DjangoTemplates`](https://docs.djangoproject.com/en/1.8/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") backend. If you’re using another template engine, [`template_name`](https://docs.djangoproject.com/en/1.8/ref/template-response/#django.template.response.SimpleTemplateResponse.template_name "django.template.response.SimpleTemplateResponse.template_name") may be a suitable alternative if you only need the name of the template used for rendering.

`resolver_match`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Response.resolver_match "Permalink to this definition")

New in Django 1.8:

An instance of [`ResolverMatch`](https://docs.djangoproject.com/en/1.8/ref/urlresolvers/#django.core.urlresolvers.ResolverMatch "django.core.urlresolvers.ResolverMatch") for the response. You can use the [`func`](https://docs.djangoproject.com/en/1.8/ref/urlresolvers/#django.core.urlresolvers.ResolverMatch.func "django.core.urlresolvers.ResolverMatch.func") attribute, for example, to verify the view that served the response:

```
# my_view here is a function based view
self.assertEqual(response.resolver_match.func, my_view)

# class-based views need to be compared by name, as the functions
# generated by as_view() won't be equal
self.assertEqual(response.resolver_match.func.__name__, MyView.as_view().__name__)

```

If the given URL is not found, accessing this attribute will raise a [`Resolver404`](https://docs.djangoproject.com/en/1.8/ref/exceptions/#django.core.urlresolvers.Resolver404 "django.core.urlresolvers.Resolver404") exception.

You can also use dictionary syntax on the response object to query the value of any settings in the HTTP headers. For example, you could determine the content type of a response using `response['Content-Type']`.

### Exceptions[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#exceptions "Permalink to this headline")

If you point the test client at a view that raises an exception, that exception will be visible in the test case. You can then use a standard `try ... except` block or [`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "(in Python v3.8)") to test for exceptions.

The only exceptions that are not visible to the test client are [`Http404`](https://docs.djangoproject.com/en/1.8/topics/http/views/#django.http.Http404 "django.http.Http404"), [`PermissionDenied`](https://docs.djangoproject.com/en/1.8/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied"), [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "(in Python v3.8)"), and [`SuspiciousOperation`](https://docs.djangoproject.com/en/1.8/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation"). Django catches these exceptions internally and converts them into the appropriate HTTP response codes. In these cases, you can check `response.status_code` in your test.

### Persistent state[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#persistent-state "Permalink to this headline")

The test client is stateful. If a response returns a cookie, then that cookie will be stored in the test client and sent with all subsequent `get()` and `post()` requests.

Expiration policies for these cookies are not followed. If you want a cookie to expire, either delete it manually or create a new `Client` instance (which will effectively delete all cookies).

A test client has two attributes that store persistent state information. You can access these properties as part of a test condition.

`Client.``cookies`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.cookies "Permalink to this definition")

A Python [`SimpleCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.SimpleCookie "(in Python v3.8)") object, containing the current values of all the client cookies. See the documentation of the [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "(in Python v3.8)") module for more.

`Client.``session`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client.session "Permalink to this definition")

A dictionary-like object containing session information. See the [session documentation](https://docs.djangoproject.com/en/1.8/topics/http/sessions/) for full details.

To modify the session and then save it, it must be stored in a variable first (because a new `SessionStore` is created every time this property is accessed):

```
def test_something(self):
    session = self.client.session
    session['somekey'] = 'test'
    session.save()

```

### Example[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#example "Permalink to this headline")

The following is a simple unit test using the test client:

```
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/customer/details/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)

```

## Provided test case classes[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#provided-test-case-classes "Permalink to this headline")

Normal Python unit test classes extend a base class of [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.8)"). Django provides a few extensions of this base class:

[![Hierarchy of Django unit testing classes (TestCase subclasses)](https://docs.djangoproject.com/en/1.8/_images/django_unittest_classes_hierarchy.svg)](https://docs.djangoproject.com/en/1.8/_images/django_unittest_classes_hierarchy.svg)

Hierarchy of Django unit testing classes

### SimpleTestCase[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#simpletestcase "Permalink to this headline")

_class_ `SimpleTestCase`[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase "Permalink to this definition")

A thin subclass of [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.8)"), it extends it with some basic functionality like:

-   Some useful assertions like:
    -   Checking that a callable [`raises a certain exception`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "django.test.SimpleTestCase.assertRaisesMessage").
    -   Testing form field [`rendering and error treatment`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertFieldOutput "django.test.SimpleTestCase.assertFieldOutput").
    -   Testing [`HTML responses for the presence/lack of a given fragment`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertContains "django.test.SimpleTestCase.assertContains").
    -   Verifying that a template [`has/hasn't been used to generate a given response content`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "django.test.SimpleTestCase.assertTemplateUsed").
    -   Verifying a HTTP [`redirect`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertRedirects "django.test.SimpleTestCase.assertRedirects") is performed by the app.
    -   Robustly testing two [`HTML fragments`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for equality/inequality or [`containment`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML "django.test.SimpleTestCase.assertInHTML").
    -   Robustly testing two [`XML fragments`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "django.test.SimpleTestCase.assertXMLEqual") for equality/inequality.
    -   Robustly testing two [`JSON fragments`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "django.test.SimpleTestCase.assertJSONEqual") for equality.
-   The ability to run tests with [modified settings](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#overriding-settings).
-   Using the [`client`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.client "django.test.SimpleTestCase.client") [`Client`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.Client "django.test.Client").
-   Custom test-time [`URL maps`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.urls "django.test.SimpleTestCase.urls").

If you need any of the other more complex and heavyweight Django-specific features like:

-   Testing or using the ORM.
-   Database [`fixtures`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures").
-   Test [skipping based on database backend features](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#skipping-tests).
-   The remaining specialized [`assert*`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.assertQuerysetEqual "django.test.TransactionTestCase.assertQuerysetEqual") methods.

then you should use [`TransactionTestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") or [`TestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase "django.test.TestCase") instead.

`SimpleTestCase` inherits from `unittest.TestCase`.

Warning

`SimpleTestCase` and its subclasses (e.g. `TestCase`, …) rely on `setUpClass()` and `tearDownClass()` to perform some class-wide initialization (e.g. overriding settings). If you need to override those methods, don’t forget to call the `super` implementation:

```
class MyTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(MyTestCase, cls).setUpClass()     # Call parent first
        ...

    @classmethod
    def tearDownClass(cls):
        ...
        super(MyTestCase, cls).tearDownClass()  # Call parent last

```

### TransactionTestCase[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#transactiontestcase "Permalink to this headline")

_class_ `TransactionTestCase`[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#TransactionTestCase)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase "Permalink to this definition")

Django’s `TestCase` class (described below) makes use of database transaction facilities to speed up the process of resetting the database to a known state at the beginning of each test. A consequence of this, however, is that some database behaviors cannot be tested within a Django `TestCase` class. For instance, you cannot test that a block of code is executing within a transaction, as is required when using [`select_for_update()`](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.select_for_update "django.db.models.query.QuerySet.select_for_update"). In those cases, you should use `TransactionTestCase`.

Changed in Django 1.8:

In older versions of Django, the effects of transaction commit and rollback could not be tested within a `TestCase`. With the completion of the deprecation cycle of the old-style transaction management in Django 1.8, transaction management commands (e.g. `transaction.commit()`) are no longer disabled within `TestCase`.

`TransactionTestCase` and `TestCase` are identical except for the manner in which the database is reset to a known state and the ability for test code to test the effects of commit and rollback:

-   A `TransactionTestCase` resets the database after the test runs by truncating all tables. A `TransactionTestCase` may call commit and rollback and observe the effects of these calls on the database.
-   A `TestCase`, on the other hand, does not truncate tables after a test. Instead, it encloses the test code in a database transaction that is rolled back at the end of the test. This guarantees that the rollback at the end of the test restores the database to its initial state.

Warning

`TestCase` running on a database that does not support rollback (e.g. MySQL with the MyISAM storage engine), and all instances of `TransactionTestCase`, will roll back at the end of the test by deleting all data from the test database and reloading initial data for apps without migrations.

Apps with migrations [will not see their data reloaded](https://docs.djangoproject.com/en/1.8/topics/testing/overview/#test-case-serialized-rollback); if you need this functionality (for example, third-party apps should enable this) you can set `serialized_rollback = True` inside the `TestCase` body.

`TransactionTestCase` inherits from [`SimpleTestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase").

### TestCase[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#testcase "Permalink to this headline")

_class_ `TestCase`[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#TestCase)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase "Permalink to this definition")

This class provides some additional capabilities that can be useful for testing Web sites.

Converting a normal [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.8)") to a Django [`TestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase "django.test.TestCase") is easy: Just change the base class of your test from `'unittest.TestCase'` to `'django.test.TestCase'`. All of the standard Python unit test functionality will continue to be available, but it will be augmented with some useful additions, including:

-   Automatic loading of fixtures.
-   Wraps the tests within two nested `atomic` blocks: one for the whole class and one for each test.
-   Creates a TestClient instance.
-   Django-specific assertions for testing for things like redirection and form errors.

_classmethod_ `TestCase.``setUpTestData`()[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#TestCase.setUpTestData)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase.setUpTestData "Permalink to this definition")

New in Django 1.8.

The class-level `atomic` block described above allows the creation of initial data at the class level, once for the whole `TestCase`. This technique allows for faster tests as compared to using `setUp()`.

For example:

```
from django.test import TestCase

class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.foo = Foo.objects.create(bar="Test")
        ...

    def test1(self):
        # Some test using self.foo
        ...

    def test2(self):
        # Some other test using self.foo
        ...

```

Note that if the tests are run on a database with no transaction support (for instance, MySQL with the MyISAM engine), `setUpTestData()` will be called before each test, negating the speed benefits.

Be careful not to modify any objects created in `setUpTestData()` in your test methods. Modifications to in-memory objects from setup work done at the class level will persist between test methods. If you do need to modify them, you could reload them in the `setUp()` method with [`refresh_from_db()`](https://docs.djangoproject.com/en/1.8/ref/models/instances/#django.db.models.Model.refresh_from_db "django.db.models.Model.refresh_from_db"), for example.

Warning

If you want to test some specific database transaction behavior, you should use `TransactionTestCase`, as `TestCase` wraps test execution within an [`atomic()`](https://docs.djangoproject.com/en/1.8/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block.

`TestCase` inherits from [`TransactionTestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase").

### LiveServerTestCase[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#liveservertestcase "Permalink to this headline")

_class_ `LiveServerTestCase`[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#LiveServerTestCase)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.LiveServerTestCase "Permalink to this definition")

`LiveServerTestCase` does basically the same as [`TransactionTestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") with one extra feature: it launches a live Django server in the background on setup, and shuts it down on teardown. This allows the use of automated test clients other than the [Django dummy client](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#test-client) such as, for example, the [Selenium](http://seleniumhq.org/) client, to execute a series of functional tests inside a browser and simulate a real user’s actions.

By default the live server’s address is `'localhost:8081'` and the full URL can be accessed during the tests with `self.live_server_url`. If you’d like to change the default address (in the case, for example, where the 8081 port is already taken) then you may pass a different one to the [`test`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-test) command via the [`--liveserver`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-option---liveserver) option, for example:

```
$ ./manage.py test --liveserver=localhost:8082

```

Another way of changing the default server address is by setting the DJANGO\_LIVE\_TEST\_SERVER\_ADDRESS environment variable somewhere in your code (for example, in a [custom test runner](https://docs.djangoproject.com/en/1.8/topics/testing/advanced/#topics-testing-test-runner)):

```
import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8082'

```

In the case where the tests are run by multiple processes in parallel (for example, in the context of several simultaneous [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) builds), the processes will compete for the same address, and therefore your tests might randomly fail with an “Address already in use” error. To avoid this problem, you can pass a comma-separated list of ports or ranges of ports (at least as many as the number of potential parallel processes). For example:

```
$ ./manage.py test --liveserver=localhost:8082,8090-8100,9000-9200,7041

```

Then, during test execution, each new live test server will try every specified port until it finds one that is free and takes it.

To demonstrate how to use `LiveServerTestCase`, let’s write a simple Selenium test. First of all, you need to install the [selenium package](https://pypi.python.org/pypi/selenium) into your Python path:

Then, add a `LiveServerTestCase`\-based test to your app’s tests module (for example: `myapp/tests.py`). For this example, we’ll assume you’re using the [`staticfiles`](https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") app and want to have static files served during the execution of your tests similar to what we get at development time with `DEBUG=True`, i.e. without having to collect them using [`collectstatic`](https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#django-admin-collectstatic). We’ll use the [`StaticLiveServerTestCase`](https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase "django.contrib.staticfiles.testing.StaticLiveServerTestCase") subclass which provides that functionality. Replace it with `django.test.LiveServerTestCase` if you don’t need that.

The code for this test may look as follows:

```
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

```

Finally, you may run the test as follows:

```
$ ./manage.py test myapp.tests.MySeleniumTests.test_login

```

This example will automatically open Firefox then go to the login page, enter the credentials and press the “Log in” button. Selenium offers other drivers in case you do not have Firefox installed or wish to use another browser. The example above is just a tiny fraction of what the Selenium client can do; check out the [full reference](http://selenium-python.readthedocs.org/en/latest/api.html) for more details.

Note

When using an in-memory SQLite database to run the tests, the same database connection will be shared by two threads in parallel: the thread in which the live server is run and the thread in which the test case is run. It’s important to prevent simultaneous database queries via this shared connection by the two threads, as that may sometimes randomly cause the tests to fail. So you need to ensure that the two threads don’t access the database at the same time. In particular, this means that in some cases (for example, just after clicking a link or submitting a form), you might need to check that a response is received by Selenium and that the next page is loaded before proceeding with further test execution. Do this, for example, by making Selenium wait until the `<body>` HTML tag is found in the response (requires Selenium > 2.13):

```
def test_login(self):
    from selenium.webdriver.support.wait import WebDriverWait
    timeout = 2
    ...
    self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
    # Wait until the response is received
    WebDriverWait(self.selenium, timeout).until(
        lambda driver: driver.find_element_by_tag_name('body'))

```

The tricky thing here is that there’s really no such thing as a “page load,” especially in modern Web apps that generate HTML dynamically after the server generates the initial document. So, simply checking for the presence of `<body>` in the response might not necessarily be appropriate for all use cases. Please refer to the [Selenium FAQ](http://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions#Q:_WebDriver_fails_to_find_elements_/_Does_not_block_on_page_loa) and [Selenium documentation](http://seleniumhq.org/docs/04_webdriver_advanced.html#explicit-waits) for more information.

## Test cases features[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#test-cases-features "Permalink to this headline")

### Default test client[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#default-test-client "Permalink to this headline")

`SimpleTestCase.``client`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.client "Permalink to this definition")

Every test case in a `django.test.*TestCase` instance has access to an instance of a Django test client. This client can be accessed as `self.client`. This client is recreated for each test, so you don’t have to worry about state (such as cookies) carrying over from one test to another.

This means, instead of instantiating a `Client` in each test:

```
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/customer/details/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        client = Client()
        response = client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)

```

…you can just refer to `self.client`, like so:

```
from django.test import TestCase

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/customer/details/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)

```

### Customizing the test client[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#customizing-the-test-client "Permalink to this headline")

`SimpleTestCase.``client_class`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.client_class "Permalink to this definition")

If you want to use a different `Client` class (for example, a subclass with customized behavior), use the [`client_class`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.client_class "django.test.SimpleTestCase.client_class") class attribute:

```
from django.test import TestCase, Client

class MyTestClient(Client):
    # Specialized methods for your environment
    ...

class MyTest(TestCase):
    client_class = MyTestClient

    def test_my_stuff(self):
        # Here self.client is an instance of MyTestClient...
        call_some_test_code()

```

### Fixture loading[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#fixture-loading "Permalink to this headline")

`TransactionTestCase.``fixtures`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.fixtures "Permalink to this definition")

A test case for a database-backed Web site isn’t much use if there isn’t any data in the database. To make it easy to put test data into the database, Django’s custom `TransactionTestCase` class provides a way of loading **fixtures**.

A fixture is a collection of data that Django knows how to import into a database. For example, if your site has user accounts, you might set up a fixture of fake user accounts in order to populate your database during tests.

The most straightforward way of creating a fixture is to use the [`manage.py dumpdata`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-dumpdata) command. This assumes you already have some data in your database. See the [`dumpdata documentation`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-dumpdata) for more details.

Note

If you’ve ever run [`manage.py migrate`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate), you’ve already used a fixture without even knowing it! When you call [`migrate`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) in the database for the first time, Django installs a fixture called `initial_data`. This gives you a way of populating a new database with any initial data, such as a default set of categories.

Fixtures with other names can always be installed manually using the [`manage.py loaddata`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-loaddata) command.

Initial SQL data and testing

Django provides a second way to insert initial data into models – the [custom SQL hook](https://docs.djangoproject.com/en/1.8/howto/initial-data/#initial-sql). However, this technique _cannot_ be used to provide initial data for testing purposes. Django’s test framework flushes the contents of the test database after each test; as a result, any data added using the custom SQL hook will be lost.

Once you’ve created a fixture and placed it in a `fixtures` directory in one of your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-INSTALLED_APPS), you can use it in your unit tests by specifying a `fixtures` class attribute on your [`django.test.TestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase "django.test.TestCase") subclass:

```
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    fixtures = ['mammals.json', 'birds']

    def setUp(self):
        # Test definitions as before.
        call_setup_methods()

    def testFluffyAnimals(self):
        # A test that uses the fixtures.
        call_some_test_code()

```

Here’s specifically what will happen:

-   At the start of each test case, before `setUp()` is run, Django will flush the database, returning the database to the state it was in directly after [`migrate`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) was called.
-   Then, all the named fixtures are installed. In this example, Django will install any JSON fixture named `mammals`, followed by any fixture named `birds`. See the [`loaddata`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-loaddata) documentation for more details on defining and installing fixtures.

This flush/load procedure is repeated for each test in the test case, so you can be certain that the outcome of a test will not be affected by another test, or by the order of test execution.

By default, fixtures are only loaded into the `default` database. If you are using multiple databases and set [`multi_db=True`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.multi_db "django.test.TransactionTestCase.multi_db"), fixtures will be loaded into all databases.

### URLconf configuration[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#urlconf-configuration "Permalink to this headline")

`SimpleTestCase.``urls`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.urls "Permalink to this definition")

Deprecated since version 1.8: Use `@override_settings(ROOT_URLCONF=...)` instead for URLconf configuration.

If your application provides views, you may want to include tests that use the test client to exercise those views. However, an end user is free to deploy the views in your application at any URL of their choosing. This means that your tests can’t rely upon the fact that your views will be available at a particular URL.

In order to provide a reliable URL space for your test, `django.test.*TestCase` classes provide the ability to customize the URLconf configuration for the duration of the execution of a test suite. If your `*TestCase` instance defines an `urls` attribute, the `*TestCase` will use the value of that attribute as the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-ROOT_URLCONF) for the duration of that test.

For example:

```
from django.test import TestCase

class TestMyViews(TestCase):
    urls = 'myapp.test_urls'

    def test_index_page_view(self):
        # Here you'd test your view using ``Client``.
        call_some_test_code()

```

This test case will use the contents of `myapp.test_urls` as the URLconf for the duration of the test case.

### Multi-database support[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#multi-database-support "Permalink to this headline")

`TransactionTestCase.``multi_db`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.multi_db "Permalink to this definition")

Django sets up a test database corresponding to every database that is defined in the [`DATABASES`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DATABASES) definition in your settings file. However, a big part of the time taken to run a Django TestCase is consumed by the call to `flush` that ensures that you have a clean database at the start of each test run. If you have multiple databases, multiple flushes are required (one for each database), which can be a time consuming activity – especially if your tests don’t need to test multi-database activity.

As an optimization, Django only flushes the `default` database at the start of each test run. If your setup contains multiple databases, and you have a test that requires every database to be clean, you can use the `multi_db` attribute on the test suite to request a full flush.

For example:

```
class TestMyViews(TestCase):
    multi_db = True

    def test_index_page_view(self):
        call_some_test_code()

```

This test case will flush _all_ the test databases before running `test_index_page_view`.

The `multi_db` flag also affects into which databases the attr:TransactionTestCase.fixtures are loaded. By default (when `multi_db=False`), fixtures are only loaded into the `default` database. If `multi_db=True`, fixtures are loaded into all databases.

### Overriding settings[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#overriding-settings "Permalink to this headline")

Warning

Use the functions below to temporarily alter the value of settings in tests. Don’t manipulate `django.conf.settings` directly as Django won’t restore the original values after such manipulations.

`SimpleTestCase.``settings`()[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.settings)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.settings "Permalink to this definition")

For testing purposes it’s often useful to change a setting temporarily and revert to the original value after running the testing code. For this use case Django provides a standard Python context manager (see [**PEP 343**](https://www.python.org/dev/peps/pep-0343)) called [`settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.settings "django.test.SimpleTestCase.settings"), which can be used like this:

```
from django.test import TestCase

class LoginTestCase(TestCase):

    def test_login(self):

        # First check for the default behavior
        response = self.client.get('/sekrit/')
        self.assertRedirects(response, '/accounts/login/?next=/sekrit/')

        # Then override the LOGIN_URL setting
        with self.settings(LOGIN_URL='/other/login/'):
            response = self.client.get('/sekrit/')
            self.assertRedirects(response, '/other/login/?next=/sekrit/')

```

This example will override the [`LOGIN_URL`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-LOGIN_URL) setting for the code in the `with` block and reset its value to the previous state afterwards.

`SimpleTestCase.``modify_settings`()[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.modify_settings)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.modify_settings "Permalink to this definition")

New in Django 1.7.

It can prove unwieldy to redefine settings that contain a list of values. In practice, adding or removing values is often sufficient. The [`modify_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.modify_settings "django.test.SimpleTestCase.modify_settings") context manager makes it easy:

```
from django.test import TestCase

class MiddlewareTestCase(TestCase):

    def test_cache_middleware(self):
        with self.modify_settings(MIDDLEWARE_CLASSES={
            'append': 'django.middleware.cache.FetchFromCacheMiddleware',
            'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
            'remove': [
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
            ],
        }):
            response = self.client.get('/')
            # ...

```

For each action, you can supply either a list of values or a string. When the value already exists in the list, `append` and `prepend` have no effect; neither does `remove` when the value doesn’t exist.

`override_settings`()[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/utils/#override_settings)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.override_settings "Permalink to this definition")

In case you want to override a setting for a test method, Django provides the [`override_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.override_settings "django.test.override_settings") decorator (see [**PEP 318**](https://www.python.org/dev/peps/pep-0318)). It’s used like this:

```
from django.test import TestCase, override_settings

class LoginTestCase(TestCase):

    @override_settings(LOGIN_URL='/other/login/')
    def test_login(self):
        response = self.client.get('/sekrit/')
        self.assertRedirects(response, '/other/login/?next=/sekrit/')

```

The decorator can also be applied to [`TestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase "django.test.TestCase") classes:

```
from django.test import TestCase, override_settings

@override_settings(LOGIN_URL='/other/login/')
class LoginTestCase(TestCase):

    def test_login(self):
        response = self.client.get('/sekrit/')
        self.assertRedirects(response, '/other/login/?next=/sekrit/')

```

Changed in Django 1.7:

Previously, `override_settings` was imported from `django.test.utils`.

`modify_settings`()[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/utils/#modify_settings)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.modify_settings "Permalink to this definition")

New in Django 1.7.

Likewise, Django provides the [`modify_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") decorator:

```
from django.test import TestCase, modify_settings

class MiddlewareTestCase(TestCase):

    @modify_settings(MIDDLEWARE_CLASSES={
        'append': 'django.middleware.cache.FetchFromCacheMiddleware',
        'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
    })
    def test_cache_middleware(self):
        response = self.client.get('/')
        # ...

```

The decorator can also be applied to test case classes:

```
from django.test import TestCase, modify_settings

@modify_settings(MIDDLEWARE_CLASSES={
    'append': 'django.middleware.cache.FetchFromCacheMiddleware',
    'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
})
class MiddlewareTestCase(TestCase):

    def test_cache_middleware(self):
        response = self.client.get('/')
        # ...

```

Note

When given a class, these decorators modify the class directly and return it; they don’t create and return a modified copy of it. So if you try to tweak the above examples to assign the return value to a different name than `LoginTestCase` or `MiddlewareTestCase`, you may be surprised to find that the original test case classes are still equally affected by the decorator. For a given class, [`modify_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") is always applied after [`override_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.override_settings "django.test.override_settings").

Warning

The settings file contains some settings that are only consulted during initialization of Django internals. If you change them with `override_settings`, the setting is changed if you access it via the `django.conf.settings` module, however, Django’s internals access it differently. Effectively, using [`override_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.override_settings "django.test.override_settings") or [`modify_settings()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") with these settings is probably not going to do what you expect it to do.

We do not recommend altering the [`DATABASES`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DATABASES) setting. Altering the [`CACHES`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-CACHES) setting is possible, but a bit tricky if you are using internals that make using of caching, like [`django.contrib.sessions`](https://docs.djangoproject.com/en/1.8/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects."). For example, you will have to reinitialize the session backend in a test that uses cached sessions and overrides [`CACHES`](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-CACHES).

Finally, avoid aliasing your settings as module-level constants as `override_settings()` won’t work on such values since they are only evaluated the first time the module is imported.

You can also simulate the absence of a setting by deleting it after settings have been overridden, like this:

```
@override_settings()
def test_something(self):
    del settings.LOGIN_URL
    ...

```

Changed in Django 1.7:

Previously, you could only simulate the deletion of a setting which was explicitly overridden.

When overriding settings, make sure to handle the cases in which your app’s code uses a cache or similar feature that retains state even if the setting is changed. Django provides the [`django.test.signals.setting_changed`](https://docs.djangoproject.com/en/1.8/ref/signals/#django.test.signals.setting_changed "django.test.signals.setting_changed") signal that lets you register callbacks to clean up and otherwise reset state when settings are changed.

Django itself uses this signal to reset various data:

 
| Overridden settings | Data reset |
| --- | --- |
| USE\_TZ, TIME\_ZONE | Databases timezone |
| TEMPLATES | Template engines |
| SERIALIZATION\_MODULES | Serializers cache |
| LOCALE\_PATHS, LANGUAGE\_CODE | Default translation and loaded translations |
| MEDIA\_ROOT, DEFAULT\_FILE\_STORAGE | Default file storage |

### Emptying the test outbox[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#emptying-the-test-outbox "Permalink to this headline")

If you use any of Django’s custom `TestCase` classes, the test runner will clear the contents of the test email outbox at the start of each test case.

For more detail on email services during tests, see [Email services](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#email-services) below.

### Assertions[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#assertions "Permalink to this headline")

As Python’s normal [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.8)") class implements assertion methods such as [`assertTrue()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "(in Python v3.8)") and [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "(in Python v3.8)"), Django’s custom [`TestCase`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class provides a number of custom assertion methods that are useful for testing Web applications:

The failure messages given by most of these assertion methods can be customized with the `msg_prefix` argument. This string will be prefixed to any failure message generated by the assertion. This allows you to provide additional details that may help you to identify the location and cause of an failure in your test suite.

`SimpleTestCase.``assertRaisesMessage`(_expected\_exception_, _expected\_message_, _callable_, _\*args_, _\*\*kwargs_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertRaisesMessage)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "Permalink to this definition")

`SimpleTestCase.``assertRaisesMessage`(_expected\_exception_, _expected\_message_)

Asserts that execution of `callable` raises `expected_exception` and that `expected_message` is found in the exception’s message. Any other outcome is reported as a failure. Similar to unittest’s [`assertRaisesRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "(in Python v3.8)") with the difference that `expected_message` isn’t a regular expression.

If only the `expected_exception` and `expected_message` parameters are given, returns a context manager so that the code being tested can be written inline rather than as a function:

```
with self.assertRaisesMessage(ValueError, 'invalid literal for int()'):
    int('a')

```

`SimpleTestCase.``assertFieldOutput`(_fieldclass_, _valid_, _invalid_, _field\_args=None_, _field\_kwargs=None_, _empty\_value=''_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertFieldOutput)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertFieldOutput "Permalink to this definition")

Asserts that a form field behaves correctly with various inputs.

<table><colgroup><col> <col></colgroup><tbody><tr><th>Parameters:</th><td><ul><li><strong>fieldclass</strong> – the class of the field to be tested.</li><li><strong>valid</strong> – a dictionary mapping valid inputs to their expected cleaned values.</li><li><strong>invalid</strong> – a dictionary mapping invalid inputs to one or more raised error messages.</li><li><strong>field_args</strong> – the args passed to instantiate the field.</li><li><strong>field_kwargs</strong> – the kwargs passed to instantiate the field.</li><li><strong>empty_value</strong> – the expected clean output for inputs in <code><span>empty_values</span></code>.</li></ul></td></tr></tbody></table>

For example, the following code tests that an `EmailField` accepts `a@a.com` as a valid email address, but rejects `aaa` with a reasonable error message:

```
self.assertFieldOutput(EmailField, {'a@a.com': 'a@a.com'}, {'aaa': ['Enter a valid email address.']})

```

`SimpleTestCase.``assertFormError`(_response_, _form_, _field_, _errors_, _msg\_prefix=''_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertFormError)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertFormError "Permalink to this definition")

Asserts that a field on a form raises the provided list of errors when rendered on the form.

`form` is the name the `Form` instance was given in the template context.

`field` is the name of the field on the form to check. If `field` has a value of `None`, non-field errors (errors you can access via [`form.non_field_errors()`](https://docs.djangoproject.com/en/1.8/ref/forms/api/#django.forms.Form.non_field_errors "django.forms.Form.non_field_errors")) will be checked.

`errors` is an error string, or a list of error strings, that are expected as a result of form validation.

`SimpleTestCase.``assertFormsetError`(_response_, _formset_, _form\_index_, _field_, _errors_, _msg\_prefix=''_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertFormsetError)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertFormsetError "Permalink to this definition")

Asserts that the `formset` raises the provided list of errors when rendered.

`formset` is the name the `Formset` instance was given in the template context.

`form_index` is the number of the form within the `Formset`. If `form_index` has a value of `None`, non-form errors (errors you can access via `formset.non_form_errors()`) will be checked.

`field` is the name of the field on the form to check. If `field` has a value of `None`, non-field errors (errors you can access via [`form.non_field_errors()`](https://docs.djangoproject.com/en/1.8/ref/forms/api/#django.forms.Form.non_field_errors "django.forms.Form.non_field_errors")) will be checked.

`errors` is an error string, or a list of error strings, that are expected as a result of form validation.

`SimpleTestCase.``assertContains`(_response_, _text_, _count=None_, _status\_code=200_, _msg\_prefix=''_, _html=False_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertContains)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertContains "Permalink to this definition")

Asserts that a `Response` instance produced the given `status_code` and that `text` appears in the content of the response. If `count` is provided, `text` must occur exactly `count` times in the response.

Set `html` to `True` to handle `text` as HTML. The comparison with the response content will be based on HTML semantics instead of character-by-character equality. Whitespace is ignored in most cases, attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

`SimpleTestCase.``assertNotContains`(_response_, _text_, _status\_code=200_, _msg\_prefix=''_, _html=False_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertNotContains)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertNotContains "Permalink to this definition")

Asserts that a `Response` instance produced the given `status_code` and that `text` does _not_ appear in the content of the response.

Set `html` to `True` to handle `text` as HTML. The comparison with the response content will be based on HTML semantics instead of character-by-character equality. Whitespace is ignored in most cases, attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

`SimpleTestCase.``assertTemplateUsed`(_response_, _template\_name_, _msg\_prefix=''_, _count=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertTemplateUsed)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "Permalink to this definition")

Asserts that the template with the given name was used in rendering the response.

The name is a string such as `'admin/index.html'`.

New in Django 1.8:

The count argument is an integer indicating the number of times the template should be rendered. Default is `None`, meaning that the template should be rendered one or more times.

You can use this as a context manager, like this:

```
with self.assertTemplateUsed('index.html'):
    render_to_string('index.html')
with self.assertTemplateUsed(template_name='index.html'):
    render_to_string('index.html')

```

`SimpleTestCase.``assertTemplateNotUsed`(_response_, _template\_name_, _msg\_prefix=''_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertTemplateNotUsed)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateNotUsed "Permalink to this definition")

Asserts that the template with the given name was _not_ used in rendering the response.

You can use this as a context manager in the same way as [`assertTemplateUsed()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "django.test.SimpleTestCase.assertTemplateUsed").

`SimpleTestCase.``assertRedirects`(_response_, _expected\_url_, _status\_code=302_, _target\_status\_code=200_, _host=None_, _msg\_prefix=''_, _fetch\_redirect\_response=True_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertRedirects)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertRedirects "Permalink to this definition")

Asserts that the response returned a `status_code` redirect status, redirected to `expected_url` (including any `GET` data), and that the final page was received with `target_status_code`.

If your request used the `follow` argument, the `expected_url` and `target_status_code` will be the url and status code for the final point of the redirect chain.

The `host` argument sets a default host if `expected_url` doesn’t include one (e.g. `"/bar/"`). If `expected_url` is an absolute URL that includes a host (e.g. `"http://testhost/bar/"`), the `host` parameter will be ignored. Note that the test client doesn’t support fetching external URLs, but the parameter may be useful if you are testing with a custom HTTP host (for example, initializing the test client with `Client(HTTP_HOST="testhost")`.

New in Django 1.7.

If `fetch_redirect_response` is `False`, the final page won’t be loaded. Since the test client can’t fetch externals URLs, this is particularly useful if `expected_url` isn’t part of your Django app.

New in Django 1.7.

Scheme is handled correctly when making comparisons between two URLs. If there isn’t any scheme specified in the location where we are redirected to, the original request’s scheme is used. If present, the scheme in `expected_url` is the one used to make the comparisons to.

`SimpleTestCase.``assertHTMLEqual`(_html1_, _html2_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertHTMLEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "Permalink to this definition")

Asserts that the strings `html1` and `html2` are equal. The comparison is based on HTML semantics. The comparison takes following things into account:

-   Whitespace before and after HTML tags is ignored.
-   All types of whitespace are considered equivalent.
-   All open tags are closed implicitly, e.g. when a surrounding tag is closed or the HTML document ends.
-   Empty tags are equivalent to their self-closing version.
-   The ordering of attributes of an HTML element is not significant.
-   Attributes without an argument are equal to attributes that equal in name and value (see the examples).

The following examples are valid tests and don’t raise any `AssertionError`:

```
self.assertHTMLEqual(
    '<p>Hello <b>world!</p>',
    '''<p>
        Hello   <b>world! <b/>
    </p>'''
)
self.assertHTMLEqual(
    '<input type="checkbox" checked="checked" id="id_accept_terms" />',
    '<input id="id_accept_terms" type="checkbox" checked>'
)

```

`html1` and `html2` must be valid HTML. An `AssertionError` will be raised if one of them cannot be parsed.

Output in case of error can be customized with the `msg` argument.

`SimpleTestCase.``assertHTMLNotEqual`(_html1_, _html2_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertHTMLNotEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLNotEqual "Permalink to this definition")

Asserts that the strings `html1` and `html2` are _not_ equal. The comparison is based on HTML semantics. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for details.

`html1` and `html2` must be valid HTML. An `AssertionError` will be raised if one of them cannot be parsed.

Output in case of error can be customized with the `msg` argument.

`SimpleTestCase.``assertXMLEqual`(_xml1_, _xml2_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertXMLEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "Permalink to this definition")

Asserts that the strings `xml1` and `xml2` are equal. The comparison is based on XML semantics. Similarly to [`assertHTMLEqual()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual"), the comparison is made on parsed content, hence only semantic differences are considered, not syntax differences. When invalid XML is passed in any parameter, an `AssertionError` is always raised, even if both string are identical.

Output in case of error can be customized with the `msg` argument.

`SimpleTestCase.``assertXMLNotEqual`(_xml1_, _xml2_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertXMLNotEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertXMLNotEqual "Permalink to this definition")

Asserts that the strings `xml1` and `xml2` are _not_ equal. The comparison is based on XML semantics. See [`assertXMLEqual()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "django.test.SimpleTestCase.assertXMLEqual") for details.

Output in case of error can be customized with the `msg` argument.

`SimpleTestCase.``assertInHTML`(_needle_, _haystack_, _count=None_, _msg\_prefix=''_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertInHTML)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML "Permalink to this definition")

Asserts that the HTML fragment `needle` is contained in the `haystack` one.

If the `count` integer argument is specified, then additionally the number of `needle` occurrences will be strictly verified.

Whitespace in most cases is ignored, and attribute ordering is not significant. The passed-in arguments must be valid HTML.

`SimpleTestCase.``assertJSONEqual`(_raw_, _expected\_data_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertJSONEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "Permalink to this definition")

Asserts that the JSON fragments `raw` and `expected_data` are equal. Usual JSON non-significant whitespace rules apply as the heavyweight is delegated to the [`json`](https://docs.python.org/3/library/json.html#module-json "(in Python v3.8)") library.

Output in case of error can be customized with the `msg` argument.

`SimpleTestCase.``assertJSONNotEqual`(_raw_, _expected\_data_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#SimpleTestCase.assertJSONNotEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertJSONNotEqual "Permalink to this definition")

New in Django 1.8.

Asserts that the JSON fragments `raw` and `expected_data` are _not_ equal. See [`assertJSONEqual()`](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "django.test.SimpleTestCase.assertJSONEqual") for further details.

Output in case of error can be customized with the `msg` argument.

`TransactionTestCase.``assertQuerysetEqual`(_qs_, _values_, _transform=repr_, _ordered=True_, _msg=None_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#TransactionTestCase.assertQuerysetEqual)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.assertQuerysetEqual "Permalink to this definition")

Asserts that a queryset `qs` returns a particular list of values `values`.

The comparison of the contents of `qs` and `values` is performed using the function `transform`; by default, this means that the `repr()` of each value is compared. Any other callable can be used if `repr()` doesn’t provide a unique or helpful comparison.

By default, the comparison is also ordering dependent. If `qs` doesn’t provide an implicit ordering, you can set the `ordered` parameter to `False`, which turns the comparison into a `collections.Counter` comparison. If the order is undefined (if the given `qs` isn’t ordered and the comparison is against more than one ordered values), a `ValueError` is raised.

Output in case of error can be customized with the `msg` argument.

Changed in Django 1.7:

The method now accepts a `msg` parameter to allow customization of error message

`TransactionTestCase.``assertNumQueries`(_num_, _func_, _\*args_, _\*\*kwargs_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#TransactionTestCase.assertNumQueries)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries "Permalink to this definition")

Asserts that when `func` is called with `*args` and `**kwargs` that `num` database queries are executed.

If a `"using"` key is present in `kwargs` it is used as the database alias for which to check the number of queries. If you wish to call a function with a `using` parameter you can do it by wrapping the call with a `lambda` to add an extra parameter:

```
self.assertNumQueries(7, lambda: my_function(using=7))

```

You can also use this as a context manager:

```
with self.assertNumQueries(2):
    Person.objects.create(name="Aaron")
    Person.objects.create(name="Daniel")

```

## Email services[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#email-services "Permalink to this headline")

If any of your Django views send email using [Django’s email functionality](https://docs.djangoproject.com/en/1.8/topics/email/), you probably don’t want to send email each time you run a test using that view. For this reason, Django’s test runner automatically redirects all Django-sent email to a dummy outbox. This lets you test every aspect of sending email – from the number of messages sent to the contents of each message – without actually sending the messages.

The test runner accomplishes this by transparently replacing the normal email backend with a testing backend. (Don’t worry – this has no effect on any other email senders outside of Django, such as your machine’s mail server, if you’re running one.)

`django.core.mail.``outbox`[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.core.mail.django.core.mail.outbox "Permalink to this definition")

During test running, each outgoing email is saved in `django.core.mail.outbox`. This is a simple list of all [`EmailMessage`](https://docs.djangoproject.com/en/1.8/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") instances that have been sent. The `outbox` attribute is a special attribute that is created _only_ when the `locmem` email backend is used. It doesn’t normally exist as part of the [`django.core.mail`](https://docs.djangoproject.com/en/1.8/topics/email/#module-django.core.mail "django.core.mail: Helpers to easily send email.") module and you can’t import it directly. The code below shows how to access this attribute correctly.

Here’s an example test that examines `django.core.mail.outbox` for length and contents:

```
from django.core import mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail('Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

```

As noted [previously](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#emptying-test-outbox), the test outbox is emptied at the start of every test in a Django `*TestCase`. To empty the outbox manually, assign the empty list to `mail.outbox`:

```
from django.core import mail

# Empty the test outbox
mail.outbox = []

```

## Management Commands[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#management-commands "Permalink to this headline")

Management commands can be tested with the [`call_command()`](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django.core.management.call_command "django.core.management.call_command") function. The output can be redirected into a `StringIO` instance:

```
from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('closepoll', stdout=out)
        self.assertIn('Expected output', out.getvalue())

```

## Skipping tests[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#skipping-tests "Permalink to this headline")

The unittest library provides the [`@skipIf`](https://docs.python.org/3/library/unittest.html#unittest.skipIf "(in Python v3.8)") and [`@skipUnless`](https://docs.python.org/3/library/unittest.html#unittest.skipUnless "(in Python v3.8)") decorators to allow you to skip tests if you know ahead of time that those tests are going to fail under certain conditions.

For example, if your test requires a particular optional library in order to succeed, you could decorate the test case with [`@skipIf`](https://docs.python.org/3/library/unittest.html#unittest.skipIf "(in Python v3.8)"). Then, the test runner will report that the test wasn’t executed and why, instead of failing the test or omitting the test altogether.

To supplement these test skipping behaviors, Django provides two additional skip decorators. Instead of testing a generic boolean, these decorators check the capabilities of the database, and skip the test if the database doesn’t support a specific named feature.

The decorators use a string identifier to describe database features. This string corresponds to attributes of the database connection features class. See `django.db.backends.BaseDatabaseFeatures` class for a full list of database features that can be used as a basis for skipping tests.

`skipIfDBFeature`(_\*feature\_name\_strings_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#skipIfDBFeature)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.skipIfDBFeature "Permalink to this definition")

Skip the decorated test or `TestCase` if all of the named database features are supported.

For example, the following test will not be executed if the database supports transactions (e.g., it would _not_ run under PostgreSQL, but it would under MySQL with MyISAM tables):

```
class MyTests(TestCase):
    @skipIfDBFeature('supports_transactions')
    def test_transaction_behavior(self):
        # ... conditional test code
        pass

```

Changed in Django 1.7:

`skipIfDBFeature` can now be used to decorate a `TestCase` class.

Changed in Django 1.8:

`skipIfDBFeature` can accept multiple feature strings.

`skipUnlessDBFeature`(_\*feature\_name\_strings_)[\[source\]](https://docs.djangoproject.com/en/1.8/_modules/django/test/testcases/#skipUnlessDBFeature)[¶](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.skipUnlessDBFeature "Permalink to this definition")

Skip the decorated test or `TestCase` if any of the named database features are _not_ supported.

For example, the following test will only be executed if the database supports transactions (e.g., it would run under PostgreSQL, but _not_ under MySQL with MyISAM tables):

```
class MyTests(TestCase):
    @skipUnlessDBFeature('supports_transactions')
    def test_transaction_behavior(self):
        # ... conditional test code
        pass

```

Changed in Django 1.7:

`skipUnlessDBFeature` can now be used to decorate a `TestCase` class.

Changed in Django 1.8:

`skipUnlessDBFeature` can accept multiple feature strings.
