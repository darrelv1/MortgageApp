# Generated by Django 4.1.5 on 2023-01-31 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0007_alter_userledger1_user_alter_userledger2_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='ledger',
        ),
    ]