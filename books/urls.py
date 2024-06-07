
from django.contrib import admin
from django.urls import path,include
app_name = 'mybooks'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mybook.urls',namespace='books'),),
]
