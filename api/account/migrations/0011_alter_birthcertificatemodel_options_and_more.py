# Generated by Django 4.1.3 on 2022-12-04 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0010_alter_birthcertificatemodel_date_of_issue_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="birthcertificatemodel",
            options={
                "verbose_name": "Свидетельство о рождении",
                "verbose_name_plural": "Свидетельства о рождении",
            },
        ),
        migrations.AlterModelOptions(
            name="foreignpassportmodel",
            options={
                "verbose_name": "Паспорт (зарубежный)",
                "verbose_name_plural": "Паспорта (зарубежные)",
            },
        ),
        migrations.AlterModelOptions(
            name="representativemodel",
            options={
                "verbose_name": "Законный представитель",
                "verbose_name_plural": "Законные представители",
            },
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-04 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_birthcertificatemodel_date_of_issue_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birthcertificatemodel',
            options={'verbose_name': 'Свидетельство о рождении', 'verbose_name_plural': 'Свидетельства о рождении'},
        ),
        migrations.AlterModelOptions(
            name='foreignpassportmodel',
            options={'verbose_name': 'Паспорт (зарубежный)', 'verbose_name_plural': 'Паспорта (зарубежные)'},
        ),
        migrations.AlterModelOptions(
            name='representativemodel',
            options={'verbose_name': 'Законный представитель', 'verbose_name_plural': 'Законные представители'},
        ),
    ]
