from rest_framework import serializers

from .models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class CreateSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    url = serializers.CharField()
    publishedAt = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data):
        return Data.objects.create(**validated_data)