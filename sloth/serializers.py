from django.contrib.auth.models import User
from rest_framework import serializers
from job.models import Proxy

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    proxies = serializers.PrimaryKeyRelatedField(many=True, queryset=Proxy.objects.all())
    print('holy shit', proxies)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'proxies')
