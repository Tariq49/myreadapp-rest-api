from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView

from apps.book.models import Author
from apps.book.serializer import AuthorSerializer


# Function-based view
@api_view(['GET']) # by default , it uses a 'GET' method, and get take as many as it handles (['GET', 'POST'])
def list_authors(request):
    # Get all authors using ORM
    authors = Author.objects.all()

    # Deserialize using the AuthorSerializer
    data = AuthorSerializer(authors, many=True)


    # Return data
    return Response(data.data, status=status.HTTP_200_OK)


class DetailAuthor(RetrieveDestroyAPIView):
    # How do we handle generic views?
    # ORM 
    queryset = Author.objects.all()

    # Serializer
    serializer_class = AuthorSerializer

class DeleteAuthor(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer