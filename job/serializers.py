from rest_framework import serializers
from job.models import Proxy


class ProxySerializer(serializers.Serializer):
    pk      = serializers.IntegerField(read_only=True)
    url     = serializers.CharField(required=False, allow_blank=True, max_length=100)
    source  = serializers.CharField(max_length=100, allow_blank=True)
    country = serializers.CharField(max_length=16, allow_blank=True)
    type    = serializers.CharField(max_length=16, allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Proxy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.url = validated_data.get('url', instance.title)
        instance.source = validated_data.get('source', instance.source)
        instance.country = validated_data.get('country', instance.country)
        instance.type= validated_data.get('type', instance.type)
        instance.save()
        return instance

    class Meta:
        model = Proxy
        fields = ('id', 'url', 'country')
