# Generated by Django 4.2.6 on 2023-10-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0004_menu_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_name',
            field=models.CharField(default='default_name', max_length=100),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]