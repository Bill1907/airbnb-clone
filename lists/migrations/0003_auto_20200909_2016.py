# Generated by Django 3.1.1 on 2020-09-09 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20200908_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='room',
            new_name='rooms',
        ),
    ]