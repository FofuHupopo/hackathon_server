# Generated by Django 4.1.3 on 2022-12-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_representativemodel_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childmodel',
            name='birthday_date',
            field=models.DateField(verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='passportmodel',
            name='date_of_issue',
            field=models.DateField(verbose_name='Дата выдачи'),
        ),
    ]