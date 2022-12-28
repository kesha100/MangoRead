from django.contrib.auth import authenticate
from rest_framework import serializers

from author.models import MyUser
from author.utils import send_activation_code, get_photo_url


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)
    image = serializers.ImageField(default="avatars/default.jpg", read_only=True)
    nickname = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirm', 'image', 'nickname')

    def get_image(self, user):
        return get_photo_url(self, user.avatar)

    def validate(self, validated_data):
        password = validated_data.get('password')
        print(validated_data)
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords do not match!')
        return validated_data

    def create(self, validated_data):
        """This function is called when self.save() method is called"""
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        if email and password:
            user = authenticate(email=email,
                                password=password)
            if not user:
                message = 'Unable to log in with provided credentials'
                raise serializers.ValidationError(message, code='authorization')

        else:
            message = 'Must include "email" and "password"'
            raise serializers.ValidationError(message, code='authorization')

        validated_data['user'] = user
        return validated_data


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the user profile.
    """

    class Meta:
        model = MyUser
        fields = "email nickname image".split()

    def validate(self, attrs):
        """
        Validate the serializer data.
        """
        queryset = MyUser.objects.exclude(id=self.context["request"].user.id)
        if queryset.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({"email": "mail already in use!"})
        if queryset.filter(nickname=attrs["nickname"]).exists():
            raise serializers.ValidationError({"nickname": "nickname already taken"})
        return attrs

