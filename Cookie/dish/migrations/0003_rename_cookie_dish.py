# Generated by Django 4.2.4 on 2023-08-28 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_cookie_delete_dish'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cookie',
            new_name='Dish',
        ),
    ]
