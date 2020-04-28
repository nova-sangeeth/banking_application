from django.conf.urls import url

from .views import index, register, profile, edit, withdraw


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^register$', register, name="register"),
    url(r'^profile$', profile, name="profile"),
    url(r'^edit$', edit, name="edit"),
    url(r'^withdraw$', withdraw, name="withdraw"),
]
