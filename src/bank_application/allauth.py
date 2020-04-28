from django.urls import reverse

from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('customer:index')

    def get_logout_redirect_url(self, request):
        return reverse('customer:index')
