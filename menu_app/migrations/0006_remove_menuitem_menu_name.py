# Generated by Django 4.2.6 on 2023-10-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0005_menuitem_menu_name_delete_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_name',
        ),
    ]
