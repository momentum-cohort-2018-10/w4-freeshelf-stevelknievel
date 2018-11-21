from django.contrib import admin
from collection.models import Book
# import model above


# create automated slug creation:
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'description',)
    prepopulated_fields = {'slug': ('title',)}


# register below:
admin.site.register(Book, BookAdmin)
