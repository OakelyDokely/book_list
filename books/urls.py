from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("account/", include("django.contrib.auth.urls")),
    path('signup/', views.SignUp.as_view(), name='signup' ),
    path("logout/", views.logout_request, name="logout"),
    path('booklist/', views.BookList.as_view(), name='booklist'),
    path('genrelist', views.GenreList.as_view(), name='genrelist'),
    path('authorlist', views.AuthorList.as_view(), name='authorlist'),
    path('addbook/', views.AddBook.as_view(), name='addbook'),
    path('addgenre/', views.AddGenre.as_view(), name='addgenre'),
    path('addauthor/', views.AddAuthor.as_view(), name='addauthor'),
    path('editauthor/<pk>', views.EditAuthor.as_view(), name='editauthor'),
    path('authorbooklist/<author>', views.authorBooks, name='authorbooks')
]