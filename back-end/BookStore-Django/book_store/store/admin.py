from django.contrib import admin

from store.models import StoreToBook, Author, Store, Book


class StoreToBookInline(admin.TabularInline):
    model = StoreToBook
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [StoreToBookInline, ]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['__str__', ]
    search_fields = ['name', 'author__full_name']
    list_filter = ['author']
    inlines = [StoreToBookInline]
    filter_horizontal = ('author',)


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    pass
