# list all tags
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.book.models import Tag
from apps.book.serializer import TagSerializer

"""

curl http://127.0.0.1:8000/api/v1/book/tag/
token_header = 'Authentication: Token '7da3ededfc2313a044c20499950703e56a6591f4'

curl -H 'Authorization: Token '7da3ededfc2313a044c20499950703e56a6591f4' http://127.0.0.1:8000/api/v1/book/tag/

"""

@api_view(['GET']) # by default , it uses a 'GET' method
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request): # JSONParser
    # Get all tags using ORM
    tags = Tag.objects.all() # Complex Data type (Querysets)

    # Deserialize using the TagSerializer
    data = TagSerializer(tags, many=True) # convert complex data types to primitive Python types


    # Return data to JSON
    return Response(data.data, status=status.HTTP_200_OK)
