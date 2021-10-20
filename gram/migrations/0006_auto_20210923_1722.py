# Generated by Django 3.2.7 on 2021-09-23 17:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0005_alter_image_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fw',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
