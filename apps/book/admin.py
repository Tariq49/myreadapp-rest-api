from django.contrib import admin
from .models import Book, Tag, Author, BookAuthor
# Register your models here.
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(BookAuthor)