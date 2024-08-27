from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Reader


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude= ('password', )

# Create Serializer for NIC


class ReaderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # set nic

    class Meta:
        model = Reader
        fields = '__all__'
        #depth = 1

