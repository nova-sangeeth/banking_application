from django.conf.urls import url

from .views import index, register, profile


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^register$', register, name="register"),
    url(r'^profile$', profile, name="profile"),
]
