from django.shortcuts import render
from django.http import HttpResponse
from .models import Winner, AILBook, Book, Recommended, BookOfTheWeek
from django.core.paginator import Paginator



def home(request):
	context = {}
	context['winner'] = Winner.objects.all().first()
	
	context['count'] = int(Book.objects.all().count())+int(AILBook.objects.all().count())

	context['book_of_the_week'] = BookOfTheWeek.objects.all().first()

	return render(request, 'library/home.html', context)



def search(request):
	if request.method=="POST":
		context = {}
		searched = request.POST['searched']
		book = Book.objects.filter(name__contains=searched)
		ail_book = AILBook.objects.filter(name__contains=searched)
		recommended_book = Recommended.objects.filter(name__contains=searched)
		
		context['searched']=searched
		context['book']=book
		context['recommended_book']=recommended_book
		context['ail_book']=ail_book

		return render(request, 'library/search.html', context)


def show_book(request, id):
	context = {}
	book = Book.objects.get(id=id)

	context['book'] = book

	return render(request, 'library/book.html', context)


def show_ail_book(request, id):
	context = {}
	ail_book = AILBook.objects.get(id=id)

	context['ail_book'] = ail_book

	return render(request, 'library/ail_book.html', context)


def show_recommended_book(request, id):
	context = {}
	recommended_book = Recommended.objects.get(id=id)

	context['recommended_book'] = recommended_book

	return render(request, 'library/recommended_book.html', context)



def ail_books(request):
	context = {}
	ail_books = AILBook.objects.all()

	context['count'] = ail_books.count()
	
	paginator = Paginator(ail_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['ail_books'] = page_obj

	return render(request, 'books/ail.html', context)


def fantasy_books(request):
	context = {}
	fantasy_books = Book.objects.filter(genre='FIC')

	context['count'] = fantasy_books.count()

	paginator = Paginator(fantasy_books, 9)
	
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['fantasy_books'] = page_obj

	return render(request, 'books/fantasy.html', context)


def business_books(request):
	context = {}
	business_books = Book.objects.filter(genre='BIZ')
	context['count'] = business_books.count()
	
	paginator = Paginator(business_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['business_books'] = page_obj

	return render(request, 'books/business.html', context)


def nofantasy_books(request):
	context = {}
	nofantasy_books = Book.objects.filter(genre='NFC')
	context['count'] = nofantasy_books.count()
	
	paginator = Paginator(nofantasy_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['nofantasy_books'] = page_obj

	return render(request, 'books/nofantasy.html', context)


def tech_books(request):
	context = {}
	tech_books = Book.objects.filter(genre='TEC')
	context['count'] = tech_books.count()
	
	paginator = Paginator(tech_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['tech_books'] = page_obj

	return render(request, 'books/tech.html', context)


def science_books(request):
	context = {}
	science_books = Book.objects.filter(genre='SCI')
	context['count'] = science_books.count()
	
	paginator = Paginator(science_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['science_books'] = page_obj

	return render(request, 'books/science.html', context)


def kids_books(request):
	context = {}
	kids_books = Book.objects.filter(genre='KID')
	context['count'] = kids_books.count()
	
	paginator = Paginator(kids_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['kids_books'] = page_obj

	return render(request, 'books/kids.html', context)


def other_books(request):
	context = {}
	other_books = Book.objects.filter(genre='O')
	context['count'] = other_books.count()
	
	paginator = Paginator(other_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['other_books'] = page_obj

	return render(request, 'books/other.html', context)


def recommended(request):
	context = {}
	recommended_books = Recommended.objects.all()
	context['count'] = recommended_books.count()
	
	paginator = Paginator(recommended_books, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['recommended_books'] = page_obj

	return render(request, 'library/recommended.html', context)	
