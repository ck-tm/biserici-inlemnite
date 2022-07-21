from django.contrib.auth import get_user_model
from rest_framework import serializers

# from rest_auth.registration.serializers import RegisterSerializer
from djoser.serializers import (
    UserCreateSerializer as BaseUserRegistrationSerializer,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {"url": {"view_name": "api:user-detail", "lookup_field": "username"}}


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ("email", "password", "first_name")


# class CustomRegisterSerializer(RegisterSerializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

#     def get_cleaned_data(self):
#         super(CustomRegisterSerializer, self).get_cleaned_data()
#         return {
#             # 'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'password2': self.validated_data.get('password2', ''),
#             'email': self.validated_data.get('email', ''),
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', '')
#         }
