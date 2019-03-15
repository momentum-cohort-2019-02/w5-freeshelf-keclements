from django.contrib import admin
from .models import Book, Author

admin.site.register(Book)
# Register your models here.
admin.site.register(Author)

