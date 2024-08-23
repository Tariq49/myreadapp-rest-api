from rest_framework import serializers
from apps.book.models import Tag
import re


class TagSerializer(serializers.ModelSerializer):

    #  def validate_name(self, value):
     #   if re.search(r'[%!@#$^&*]', value):
      #      raise serializers.ValidationError("Tag name cannot contain characters like %!@#$^&*")
       # return value
    def validate_name(self, value):
        if any(char in value for char in '%!&*#'):
            raise serializers.ValidationError('name should not contain special characters')
        return value

    name = serializers.SerializerMethodField(read_only=True)


   

    def get_name(self, obj):
        """Return the capitalized version of the tag's name."""
        return obj.name.capitalize()

  
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id', )