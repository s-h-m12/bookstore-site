from django.shortcuts import render
from .models import Books
from django.db.models import Q

def search(request):
   books = Books.objects.all()

   search_book = request.GET.get('search', '')
   if search_book:
      books = books.filter(
         Q(title__icontains=search_book) |
         Q(author__icontains=search_book)
      )



   return render(request,'search.html', {
      'books': books,
      'search_book': search_book,

   })

def filterer(request):
   books = Books.objects.all()

   genre_filter = request.GET.get('genre', None)
   if genre_filter:  # Фильтрация по жанру
      books = books.filter(genre=genre_filter)

   return render(request,'filterer.html',{
      'books': books,
      'genre_filter': genre_filter,

   })


def index(request):
   return render(request,'index.html')