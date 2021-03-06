# Generated by Django 3.2.7 on 2021-09-19 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=350)),
                ('profile_pic', models.ImageField(upload_to='ProfilePicture/')),
                ('profile_avatar', models.ImageField(upload_to='AvatarPicture/')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictsgram/')),
                ('image_caption', models.CharField(max_length=700)),
                ('tag_someone', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_link', models.ManyToManyField(blank=True, default=False, related_name='likes', to='gram.Profile')),
                ('imageuploader_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_post', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='gram.profile')),
                ('commented_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.image')),
            ],
        ),
    ]
