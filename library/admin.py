from django.contrib import admin
from .models import Winner, AILBook, Book, Recommended, BookOfTheWeek

admin.site.register(Winner)
admin.site.register(BookOfTheWeek)
admin.site.register(AILBook)
admin.site.register(Book)
admin.site.register(Recommended)