# Generated by Django 2.2.1 on 2022-03-16 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0011_auto_20220316_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='titles',
            new_name='title',
        ),
    ]