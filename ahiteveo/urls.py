from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'users.views.home'),
    # url(r'^blog/', include('blog.urls')),
    #USUARIOS
    url(r'^login/$', 'users.views.loguet_in'),
    url(r'^perfil/$', 'users.views.private'),
    url(r'^user/resetpass/$', 'users.views.reset_pass'),
    url(r'^logout/$', 'users.views.loguet_out'),
    url(r'^user/new/$', 'users.views.new_user'),
    url(r'^user/confirmar/$', 'users.views.confirmation_user'),

    #PROFILES
    url(r'^profile/complete/$', 'users.views.complete_profile'),

    
)
