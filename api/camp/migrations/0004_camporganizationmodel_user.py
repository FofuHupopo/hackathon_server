# Generated by Django 4.1.3 on 2022-12-04 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camp', '0003_alter_campeventmodel_camp_organization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camporganizationmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
