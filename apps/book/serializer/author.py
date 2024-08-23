from rest_framework import serializers
from apps.book.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    #TODO: specify the model that this serializer will link to
    # TODO: Specify which fields should be considered in the model

    # Force django REST to recognize the method
    name = serializers.CharField(read_only=True) # read-only
    # create a serialized method
    username = serializers.SerializerMethodField()

    # Serialized method's implementation
    def get_username(self, obj): # get <serializer_method_field>
        return '_'.join([obj.first_name, obj.last_name])

    def validate_first_name(self, value): # validate_<field-name>
        """Field-level Validation"""
        if '-' in value:
            # TODO: Always raise a validation exception when condition fails
            raise serializers.ValidationError('First name should not contain hyphen (-)')
        
        # TODO: If condition is true, then return the value
        return value


    def validate(self, attrs):
        """Object-level Validation"""
        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('First name and last name should not be the same')
        
        return attrs

 
    class Meta:
        model = Author
        fields = '__all__' # ('id', 'first_name')
        read_only_fields = ('id', )


