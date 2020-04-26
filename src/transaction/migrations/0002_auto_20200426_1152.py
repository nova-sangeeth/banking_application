# Generated by Django 3.0.5 on 2020-04-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_model',
            name='type',
            field=models.CharField(choices=[('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit'), ('Account transfer', 'Account Transfer')], max_length=128),
        ),
    ]
