# Generated by Django 4.1.3 on 2022-12-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_childmodel_citizenship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthcertificatemodel',
            name='date_of_issue',
            field=models.DateField(verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='foreignpassportmodel',
            name='date_of_issue',
            field=models.DateField(verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='foreignpassportmodel',
            name='duration',
            field=models.DateField(null=True, verbose_name='Срок действия'),
        ),
        migrations.AlterField(
            model_name='russianpassportmodel',
            name='date_of_issue',
            field=models.DateField(verbose_name='Дата выдачи'),
        ),
    ]
