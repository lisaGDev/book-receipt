# Generated by Django 4.2.4 on 2023-08-29 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0003_rename_cookie_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='id_dish',
        ),
    ]