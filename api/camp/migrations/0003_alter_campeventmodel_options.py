# Generated by Django 4.1.3 on 2022-12-04 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("camp", "0002_rename_сampeventmodel_campeventmodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="campeventmodel",
            options={"verbose_name": "Смена", "verbose_name_plural": "Смены"},
        ),
    ]
