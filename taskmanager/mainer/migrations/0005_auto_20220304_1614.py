# Generated by Django 2.2.1 on 2022-03-04 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0004_auto_20220304_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qaz',
            old_name='task',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='qaz1',
            old_name='task1',
            new_name='conten1',
        ),
        migrations.RenameField(
            model_name='qaz2',
            old_name='task2',
            new_name='content2',
        ),
        migrations.RenameField(
            model_name='qaz3',
            old_name='task3',
            new_name='content3',
        ),
    ]
