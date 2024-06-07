from django.contrib import admin
from mybook.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book,BookAdmin)