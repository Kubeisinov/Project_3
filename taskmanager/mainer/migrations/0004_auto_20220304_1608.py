# Generated by Django 2.2.1 on 2022-03-04 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0003_auto_20220304_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qaz1',
            old_name='task',
            new_name='task1',
        ),
        migrations.RenameField(
            model_name='qaz2',
            old_name='task',
            new_name='task2',
        ),
        migrations.RenameField(
            model_name='qaz3',
            old_name='task',
            new_name='task3',
        ),
    ]
