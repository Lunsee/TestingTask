# Generated by Django 4.2.6 on 2023-10-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0006_remove_menuitem_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='named_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
