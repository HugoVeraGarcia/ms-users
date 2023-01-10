from rest_framework.serializers import Serializer, FileField, ModelSerializer
from .models import User

class UploadSerializer(Serializer):

    file_upload = FileField()

    class Meta:
        fields = ['file_upload']



class UserSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = ["id", "name", "email", "password"]
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
