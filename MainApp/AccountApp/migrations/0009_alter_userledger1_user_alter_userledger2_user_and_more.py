# Generated by Django 4.1.5 on 2023-01-31 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0008_remove_userprofile_ledger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userledger1',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AccountApp.userprofile'),
        ),
        migrations.AlterField(
            model_name='userledger2',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AccountApp.userprofile'),
        ),
        migrations.AlterField(
            model_name='userledger3',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AccountApp.userprofile'),
        ),
    ]
