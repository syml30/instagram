from rest_framework import serializers
from .models import Setting, Like


class SettingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"

    # def create(self, validated_data):
    #     return Setting.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.first_name = validate_data.get("first_name", instance.first_name)
        instance.last_name = validate_data.get("last_name", instance.last_name)
        instance.status = validate_data.get("status", instance.status)
        instance.image_setting = validate_data.get("image_setting", instance.image_setting)

        instance.save()
        return instance
    #
    # def delete(self, instance):
    #     pass


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id"]
