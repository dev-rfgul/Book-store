from django.db import models

# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length =  20)
	last_name = models.CharField(max_length = 20)
	bio = models.TextField(default = "")

class Publisher(models.Model):
	title = models.CharField(max_length = 30)
	country = models.CharField(max_length = 20)


class Book(models.Model):
	title = models.CharField(max_length = 30)
	pages = models.IntegerField()
	edition = models.IntegerField()
	publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE, related_name = 'books')
	authors = models.ManyToManyField(Author, related_name = 'books')




