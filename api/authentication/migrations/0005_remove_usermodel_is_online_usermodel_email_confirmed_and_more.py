# Generated by Django 4.1.3 on 2022-12-03 15:06

import api.authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_usermodel_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_online',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='Почта подверждена?'),
        ),
        migrations.CreateModel(
            name='ConfirmCodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, verbose_name='Код')),
                ('lifetime', models.DateTimeField(default=api.authentication.models.code_lifetime, verbose_name='Жив до')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Для пользователя')),
            ],
            options={
                'verbose_name': 'Код',
                'verbose_name_plural': 'Коды',
                'db_table': 'auth__confirm_code',
            },
        ),
    ]
