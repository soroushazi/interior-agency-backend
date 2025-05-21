from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_image = serializers.ImageField(read_only=True)  # Make sure to add this

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'password',
            'full_name', 'phone_number', 'is_designer', 'is_client', 'profile_image'
        ]

    def get_profile_image(self, obj):
        request = self.context.get('request')
        if obj.profile_image and request:
            return request.build_absolute_uri(obj.profile_image.url)
        return None

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

