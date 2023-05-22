from rest_framework import serializers
from .models import App, AdminUser, User, Profile, downloadApp


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["app_name", "app_category", "app_point", "app_icon"]


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = Profile
        fields = ['image', 'user']


class downloadAppSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = downloadApp
        fields = ['screenshot', 'app']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.user.username
        representation['app'] = instance.app.app_name
        representation['points'] = instance.app.app_point
        representation['app_id'] = instance.id
        return representation
