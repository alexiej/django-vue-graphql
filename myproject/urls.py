from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
import os


from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url=os.path.join(settings.STATIC_URL,'favicon.ico'), permanent=True)

urlpatterns = [
    path('favicon.ico', favicon_view),
    path('', TemplateView.as_view(template_name='index.html')),
    path('about/', TemplateView.as_view(template_name='index.html')),    
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),    
    path('admin/', admin.site.urls),

    #DJANGO folders
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    url(r'^dmedia/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),

    #Vue.js folders
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
    url(r'^img/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'img')}),
    url(r'^js/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'js')}),
    url(r'^css/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'css')}),
    url(r'^fonts/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'fonts')}),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns