from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
        ('About book', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

class BooksInstanceInline(admin.StackedInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInline(admin.StackedInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('first_name', 'last_name')
        }),
        ('Dates', {
            'fields': ('date_of_birth', 'date_of_death')
        })
    )
    inlines = [BookInline]

admin.site.register(Genre)