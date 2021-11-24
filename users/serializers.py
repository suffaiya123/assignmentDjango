from rest_framework import fields, serializers
from users.models import CustomUser
from django.contrib.auth.hashers import make_password


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "dob",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        first_name = attrs["first_name"]
        if first_name == "" or first_name is None:
            raise serializers.ValidationError("first_name should not be null or None")
        return super().validate(attrs)

    def create(self, validated_data):

        if validated_data.get("password"):
            validated_data["password"] = make_password(validated_data["password"])
        return super(CreateProfileSerializer, self).create(validated_data)


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "dob",
        ]
        read_only_fields = ["email", "phone_number"]
