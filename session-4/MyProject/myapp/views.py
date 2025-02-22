from django.shortcuts import render, get_object_or_404, redirect
#To use our model
from .models import Book
#To use datetime
from datetime import datetime

def book_list(request):
    #We wanted to show all books so we got them all
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        #Get what we enter in HTML and put them in these variables, then pass them to model
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'book_create.html')

def book_update(request, pk):
    #Find the book we want to update by pk since they are uique for each book
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        #Save things we did
        book.save()
        return redirect('book_list')
    return render(request, 'book_update.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
