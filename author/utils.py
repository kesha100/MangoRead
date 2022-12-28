import os
from uuid import uuid4

from rest_framework import serializers
from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    """sends activation link to console, by click to this link it activates your account"""
    activation_url = f'http://localhost:8000/api/v1/account/activate/{activation_code}'
    message = f"""
        Thank you for signing up in MangoRead!
        Please, activate your account.
        Activation link: {activation_url}
    """
    send_mail(
        'Activate your account',
        message,
        'fromaru@gmail.com',
        [email, ],
        fail_silently=False
    )


def get_photo_url(serializer: serializers.ModelSerializer, photo):
    return serializer.context['request'].build_absolute_uri(photo.url)


def user_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'avatars/{}/{}.{}'.format(instance.email, uuid4().hex, ext)
