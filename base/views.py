from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def get_books(request, pk=None):
    
    if pk:
        if Book.objects.filter(id=pk).exists():
            books = Book.objects.filter(id=pk)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        return Response({"error": "Book with id {} does not exist".format(pk)})
    
    
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
