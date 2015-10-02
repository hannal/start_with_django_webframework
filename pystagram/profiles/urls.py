from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<username>[\w.@+-]+)/$',
        views.profile,
        name='profile'
    ),
]
