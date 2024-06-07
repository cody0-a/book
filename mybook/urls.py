from django.urls import path
from . import views
app_name = 'mybook'
urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
]