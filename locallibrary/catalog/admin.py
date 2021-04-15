from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

# Create inline BooksInstance
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Create inline Books
class Books(admin.TabularInline):
    model = Book

# Define the admin class ，因為看起來亂所以先不註冊
#@admin.register(Author)  
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [Books]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)  	
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('imprint', 'status', 'due_back')

    fieldsets = (
        ('Contains', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )