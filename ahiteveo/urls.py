from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Examples:
    url(r'^$', 'users.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #USUARIOS
    url(r'^user/new/$', 'users.views.new_user'),
    url(r'^login/$', 'users.views.loguet_in'),
    url(r'^logout/$', 'users.views.loguet_out'),
    url(r'^perfil/$', 'users.views.index_perfil'),
    url(r'^user/confirmar/$', 'users.views.confirmation_user'),
    url(r'^user/resetpass/$', 'users.views.reset_pass'),
    url(r'^user/perfil/new/$', 'users.views.complete_perfil'),
    url(r'^user/perfil/edit/$', 'users.views.edit_perfil'),

    #CATEGORIAS
    url(r'^category/$', 'productos.views.index'),
    url(r'^category/new/$', 'productos.views.new_categoria'),

    #TIPO
    url(r'^type/new/$', 'productos.views.new_tipo'),

    url(r'^type/search/ajax/$', 'productos.views.buscar_tipo_ajax'),

    #PRODUCTOS
    url(r'^product/$', 'productos.views.index_productos'),
    url(r'^product/new/$', 'productos.views.new_producto'),

    url(r'^product/(?P<producto_id>\d+)/imagen/new$', 'productos.views.new_imagen'),
)