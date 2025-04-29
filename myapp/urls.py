
from . import views
from django.urls import path
urlpatterns = [
path ('Hi/', views.greeting),
path('Message/', views.message),
path('', views.home, name = "index"),
path('about-us/', views.about, name ="about"),
path('we-offer/', views.service, name ="service"),
path('response/', views.response, name ="response"),
path('form/', views.form_submit, name ="form_submit"),
path('edit/<str:username>/', views.edit, name = 'edit'),
path('full-form/', views.full_form, name = 'full_form'),


path('create_author/', views.create_author, name = 'create_author'),
path('authors/', views.get_authors, name = 'get_authors'),
path('delete_author/<int:pk>/', views.delete_author, name = 'delete_author'),
path('edit_author/<int:pk>/', views.edit_author, name = 'edit_author'),

path('create_book/', views.create_book, name = 'create_book'),
path('create_publisher/', views.create_publisher, name = 'create_publisher'),
path('books/', views.get_books, name = 'books'),
path('edit_book/<int:pk>', views.edit_book, name = 'edit_book'),
path('delete_book/<int:pk>', views.delete_book, name = 'delete_book'),

path('publishers/', views.get_publishers, name = 'get_publishers'),
path('edit_publisher/<int:pk>', views.edit_publisher, name = 'edit_publisher'),
path('delete_publisher/<int:pk>', views.delete_publisher, name = 'delete_publisher'),
path('books_by_author/<int:pk>', views.get_book_by_authors, name = 'get_book_by_authors'),
]