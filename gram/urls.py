from django.contrib import admin
from django.urls import path
from .views import user_register, user_login, ImageList, MyFollowerImages, search, SettingList, SettingDetail, \
    LikeCreate

urlpatterns = [

    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('images_list/', ImageList.as_view()),
    path('my_follower_images/', MyFollowerImages.as_view()),
    path('search/', search, name='search'),
    path('setting/', SettingList.as_view()),
    path('setting_detail/<int:pk>', SettingDetail.as_view()),
    path('api/posts/<int:pk>', LikeCreate.as_view()),


]
