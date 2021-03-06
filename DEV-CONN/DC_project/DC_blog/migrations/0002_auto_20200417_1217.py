# Generated by Django 3.0.3 on 2020-04-17 12:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DC_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(blank=True, default='coding.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='gitpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='gitpost',
            name='repo_addr',
            field=models.URLField(max_length=2083),
        ),
        migrations.AlterField(
            model_name='gitpost',
            name='repo_desc',
            field=models.TextField(max_length=200),
        ),
    ]
