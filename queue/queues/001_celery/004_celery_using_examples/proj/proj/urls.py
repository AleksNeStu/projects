from django.conf import settings
from django.conf.urls import handler500, handler404  # noqa
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path as url  # noqa
from django.views import defaults as default_views
from django.views.generic import TemplateView

from tasks.views import ReportErrorView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'src.views.home', name='home'),
#     # url(r'^proj/', include('src.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# ]


urlpatterns = [
                  url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
                  url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
                  url(r'^report-error/', ReportErrorView.as_view(), name='report-error'),

                  # Django Admin, use {% url 'admin:index' %}
                  url(settings.ADMIN_URL, admin.site.urls),

                  # Your stuff: custom urls includes go here

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
