from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import BookForm, GenreForm, AuthorForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.db.models import Count

from .models import Book, Genre, Author

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'

class AddBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/add_book.html'

class GenreList(ListView):
    model = Genre
    template_name = 'books/genre_list.html'

class AddGenre(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'books/add_genre.html'

class AuthorList(ListView):
    model = Author
    template_name = 'books/author_list.html'
    book_count = Book.objects.annotate(num_books=Count("author"))
    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        context.update({
            'books': Book.objects.all(),
        })
        return context

class AddAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/add_author.html'

class EditAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/edit_author.html'

def authorBooks(request, author):
    books = Book.objects.all()
    context = {'books' : books, 'author' : author.replace("-", " ")}
    return render(request, 'books/author_book_list.html', context)

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_request(request):
  logout(request)
  return redirect("home")