# Generated by Django 2.2.1 on 2022-04-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0019_auto_20220421_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['name'], 'verbose_name': 'Регистрация', 'verbose_name_plural': 'Регистрация'},
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='telnumber',
            new_name='tel_number',
        ),
    ]
