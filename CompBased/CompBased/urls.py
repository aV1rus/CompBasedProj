from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CompBased.views.home', name='home'),
    # url(r'^CompBased/', include('CompBased.foo.urls')),

    url(r'^$', 'Login.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup-email/', 'Login.views.signup_email'),
    url(r'^email-sent/', 'Login.views.validation_sent'),
    url(r'^login/$', 'Login.views.home'),
    url(r'^done/$', 'Login.views.done', name='done'),
    url(r'^email/$', 'Login.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^home/', include('Home.urls'))

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
