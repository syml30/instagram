# Generated by Django 3.2.7 on 2021-09-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_profile_fw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_link',
            field=models.ManyToManyField(blank=True, related_name='likes', to='gram.Profile'),
        ),
    ]
