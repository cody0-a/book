from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

app_name = "mybook"
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = "books/booklist.html"
    def perform_create(self, serializer):
        if self.request.user == None:
            self.request.user = self.request.user
        else:
            pass 
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
    

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = "books/bookupdate.html"

   
