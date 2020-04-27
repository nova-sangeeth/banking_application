# Generated by Django 3.0.5 on 2020-04-27 14:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_loans_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('transaction_time', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('transaction_id', models.CharField(max_length=128)),
                ('loan_id', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('auto', 'auto_loans'), ('personal', 'personal_loans'), ('home', 'home_loans'), ('student', 'student_loans')], max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
