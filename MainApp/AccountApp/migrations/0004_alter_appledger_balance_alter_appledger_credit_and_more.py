# Generated by Django 4.1.5 on 2023-01-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AccountApp", "0003_appledger_appprofile_rename_ledgers_ledger_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appledger",
            name="balance",
            field=models.IntegerField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="appledger", name="credit", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="appledger", name="date", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="appledger", name="debit", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="ledger", name="credit", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="ledger", name="date", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="ledger", name="debit", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="userprofile", name="rate", field=models.IntegerField(null=True),
        ),
    ]
