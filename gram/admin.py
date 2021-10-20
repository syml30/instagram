from django.contrib import admin

from .models import Profile, Image, Comments, Setting, Like

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Setting)
admin.site.register(Like)
