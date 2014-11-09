from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^photo/(?P<photo_id>\d+)$', 'photo.views.single_photo', name='view_single_photo'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static('static_files', document_root=settings.MEDIA_ROOT)
