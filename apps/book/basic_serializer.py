from rest_framework import serializers
from apps.book.models.author import Author
from apps.book.models.tag import Tag



# Author serializer
class AuthorSerializer(serializers.Serializer): # <model>Serializer
    id = serializers.IntegerField(read_only=True) # field-level
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def create(self, validated_data):
        return Author.objects.get_or_create(**validated_data)
    

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Tag.objects.get_or_create(**validated_data)