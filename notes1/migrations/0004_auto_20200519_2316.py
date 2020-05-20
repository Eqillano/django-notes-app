# Generated by Django 2.2 on 2020-05-19 20:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes1', '0003_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favourite',
        ),
        migrations.AddField(
            model_name='post',
            name='favourite',
            field=models.ManyToManyField(related_name='favs', to=settings.AUTH_USER_MODEL),
        ),
    ]