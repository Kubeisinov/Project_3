# Generated by Django 2.2.1 on 2022-03-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0009_auto_20220305_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=60, verbose_name='Name')),
                ('info', models.TextField(verbose_name='Info')),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]
