from django.contrib import admin
from .models import Book
from .models import Borrower




class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_available')
    search_fields = ('title', 'author')
    list_filter = ('is_available', )

# admin.site.register(Book) --> we first write this, then add class and write below
admin.site.register(Book, BookAdmin)

admin.site.register(Borrower)

admin.site.site_header = "Library Management System"

