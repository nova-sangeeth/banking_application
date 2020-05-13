from django.conf.urls import url
from .views import employee_profile
urlpatterns = [
    url(r'^employee_profile$', employee_profile, name='employee_profile'),
]
