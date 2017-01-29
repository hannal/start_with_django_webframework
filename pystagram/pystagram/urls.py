from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from photos.views import hello
from photos.views import detail
from photos.views import create


urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^photos/upload/$', create, name='create'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)

