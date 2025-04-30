from django.db import models

# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length =  20)
	last_name = models.CharField(max_length = 20)
	bio = models.TextField(default = "")

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
	title = models.CharField(max_length = 30)
	country = models.CharField(max_length = 20)
	def __str__(self):
		return self.title + " " + self.country


class Book(models.Model):
	title = models.CharField(max_length = 30)
	pages = models.IntegerField()
	edition = models.IntegerField()
	publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE, related_name = 'books')
	authors = models.ManyToManyField(Author, related_name = 'books')
	def __str__(self):
		return self.title 




