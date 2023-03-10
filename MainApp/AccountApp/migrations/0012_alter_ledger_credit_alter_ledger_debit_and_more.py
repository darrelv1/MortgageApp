# Generated by Django 4.1.5 on 2023-02-09 06:05

import AccountApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0011_alter_userledger1_options_alter_userledger2_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='credit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_negative]),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='debit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_positive]),
        ),
        migrations.AlterField(
            model_name='userledger1',
            name='credit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_negative]),
        ),
        migrations.AlterField(
            model_name='userledger1',
            name='debit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_positive]),
        ),
        migrations.AlterField(
            model_name='userledger2',
            name='credit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_negative]),
        ),
        migrations.AlterField(
            model_name='userledger2',
            name='debit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_positive]),
        ),
        migrations.AlterField(
            model_name='userledger3',
            name='credit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_negative]),
        ),
        migrations.AlterField(
            model_name='userledger3',
            name='debit',
            field=models.IntegerField(default=0, validators=[AccountApp.models.validator_not_positive]),
        ),
    ]
