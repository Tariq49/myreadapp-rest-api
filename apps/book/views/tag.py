# list all tags
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.book.models import Tag
from apps.book.serializer import TagSerializer

@api_view(['GET']) # by default , it uses a 'GET' method
def list_tags(request): # JSONParser
    # Get all tags using ORM
    tags = Tag.objects.all() # Complex Data type (Querysets)

    # Deserialize using the TagSerializer
    data = TagSerializer(tags, many=True) # convert complex data types to primitive Python types


    # Return data to JSON
    return Response(data.data, status=status.HTTP_200_OK)
