from django.urls import path
from .views import home,search,show_book,show_ail_book,recommended
from .views import ail_books, fantasy_books, business_books, nofantasy_books
from .views import tech_books, science_books, other_books, kids_books, show_recommended_book


urlpatterns = [
	path('', home, name='home'),
	path('search/', search, name='search'),
	path('show_book/<str:id>', show_book, name='show_book'),
	path('show_ail_book/<str:id>', show_ail_book, name='show_ail_book'),
	path('show_recommended_book/<str:id>', show_recommended_book, name='show_recommended_book'),
	path('recommended/', recommended, name='recommended'),
	path('ail/', ail_books, name='ail'),
	path('fantasy/', fantasy_books, name='fantasy'),
	path('business/', business_books, name='business'),
	path('nofantasy/', nofantasy_books, name='nofantasy'),
	path('tech/', tech_books, name='tech'),
	path('science/', science_books, name='science'),
	path('kids/', kids_books, name='kids'),
	path('other/', other_books, name='other'),
]