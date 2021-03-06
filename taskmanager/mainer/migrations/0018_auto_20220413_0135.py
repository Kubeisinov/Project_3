# Generated by Django 2.2.1 on 2022-04-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainer', '0017_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='anonymous', max_length=30),
        ),
        migrations.AddField(
            model_name='posts',
            name='describe',
            field=models.TextField(default='DataFlair Django tutorials'),
        ),
        migrations.AddField(
            model_name='posts',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='posts',
            name='picture',
            field=models.ImageField(default='default value', upload_to=''),
        ),
    ]
