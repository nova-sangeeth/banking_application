from django_tables2 import tables

from django.contrib.auth.models import User


class user_list_table(tables.Table):
    class Meta:
        model = User
        fields = ('Username', 'email')
