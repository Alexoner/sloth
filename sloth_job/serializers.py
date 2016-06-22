from rest_framework import serializers
from .models import Proxy


class ProxySerializer(serializers.Serializer):
    pk      = serializers.IntegerField(read_only=True)
    owner   = serializers.ReadOnlyField(source='owner.username')
    created = serializers.CharField(required=False)
    address = serializers.CharField(required=False, allow_blank=True, max_length=100)
    source  = serializers.CharField(max_length=100, allow_blank=True)
    country = serializers.CharField(max_length=16, allow_blank=True)
    type    = serializers.CharField(max_length=16, allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Proxy` instance, given the validated data.
        """
        return Proxy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing instance, given the validated data.
        """
        instance.address = validated_data.get('address', instance.address)
        instance.source  = validated_data.get('source', instance.source)
        instance.country = validated_data.get('country', instance.country)
        instance.type    = validated_data.get('type', instance.type)
        instance.save()
        return instance

    class Meta:
        model = Proxy
        fields = ('id', 'owner', 'address', 'country', 'type', 'created')
