from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', 'login.views.connect'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^signup-email/', 'login.views.signup_email'),
    # url(r'^email-sent/', 'login.views.validation_sent'),
    url(r'^login/$', 'login.views.connect'),
    # url(r'^email/$', 'login.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^home/', include('home.urls')),
    url(r'^register/', "login.views.register"),
    url(r'^logout/', "login.views.disconnect"),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns() #Used only in debug mode
