# Generated by Django 4.2.6 on 2023-10-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_name',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
