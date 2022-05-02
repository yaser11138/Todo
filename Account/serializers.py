from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(User.objects.all())])

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email", "first_name", "last_name")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, data, ):
        if data.get("password") != data.get("password2"):
            return serializers.ValidationError("The two password fields didn't match.")
        return data

    def create(self, validated_data):
        user = User(username=validated_data["username"], email=validated_data["email"],
                    first_name=validated_data["first_name"], last_name=validated_data["last_name"])
        user.set_password(validated_data["password"])
        user.save()
        return user
