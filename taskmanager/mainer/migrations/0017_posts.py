# Generated by Django 2.2.1 on 2022-04-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0016_delete_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тақырып')),
                ('is_published', models.BooleanField(default=True, verbose_name=' ')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
    ]