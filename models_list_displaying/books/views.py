from django.shortcuts import render
from books.models import Book



def books_view(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    print(all_books)



    context = {'books': all_books}
    #context = {}
    return render(request, template, context)

def books(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    print(all_books)



    context = {'book': all_books}
    #context = {}
    return render(request, template, context)