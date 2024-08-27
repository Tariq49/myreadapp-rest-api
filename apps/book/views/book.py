from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.book.models import Book, Author
from apps.book.serializer import ReadBookSerializer, CreateBookSerializer

# List Book




@api_view(['GET']) # by default , it uses a 'GET' method
def list_books(request):

    # Get all books using ORM
    books= Book.objects.all()

    # Deserialize using the AuthorSerializer
    data = ReadBookSerializer(books, many=True)


    # Return data
    return Response(data.data, status=status.HTTP_200_OK)


# Create Book
@api_view(['POST']) 
def create_book(request):
    with transaction.atomic():
        data= request.data # retrieve the request body in native Python data types
       
        authors = data['authors']
   
        book = CreateBookSerializer(data=data)

        book.is_valid()
        saved_book = book.save()

        # add authors
        for author in authors:
            author_obj = Author.objects.get(pk=author['id'])
            saved_book.authors.add(author_obj, through_defaults={'role': author['role']})

    # Return a JSON transformed data
    return Response({'isbn': saved_book.isbn}, status=status.HTTP_201_CREATED)
    
    # return Response({'detail': 'Invalid request data', 'error': 'Invalid_Request'}, status=status.HTTP_400_BAD_REQUEST)


class BooksView(APIView):
    # GET
    def get(self, request):
        # GET books from database using ORM
        books = Book.objects.all()

        # Deserialization
        data = ReadBookSerializer(books, many=True)

        # Return JSON
        return Response({'data': data.data}, status=status.HTTP_200_OK)
    

    # POST
    def post(self, request):
        pass

    # DELETE
    def delete(self, request):
        pass

    # PUT
    def put(self, request):
        pass

    # PATCH
    def patch(self, request):
        pass
