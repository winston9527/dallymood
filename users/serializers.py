from django.core.validators import RegexValidator
from rest_framework import serializers

from users.models import Users
from utils import encrypt


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, min_length=8, max_length=20)
    role = serializers.CharField(required=True, validators=[RegexValidator(r'^(manager|customer|doctor)$', 'role is '
                                                                                                           'invalid')])

    class Meta:
        model = Users
        fields = '__all__'

    def validate_password(self, password):
        encrypt_pwd = encrypt.md5(password)
        return encrypt_pwd
