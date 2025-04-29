from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Author, Publisher, Book


# Create your views here.
def get_book_by_authors(request, pk):
	author = Author.objects.get(id = pk)
	author.books.all()

def create_author(request):
	if request.method == "POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		bio = request.POST.get("bio")

		author = Author.objects.create(first_name = first_name, last_name = last_name, bio = bio)

		return HttpResponse(f"An abject is created with an ID of {author.id}")
	
	else:
		return render(request, 'create_author.html')

def get_authors(request):
	authors = Author.objects.all()

	context = {'authors':authors}

	return render(request, 'authors.html', context)

	#Author.objects.get(first_name = "" , last_name = "")

def edit_author(request, pk):
	author=get_object_or_404(Author, id = pk)
	if request.method == "GET":
		context = {'author': author}
		return render(request, 'edit_author.html', context)
	elif request.method == "POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		bio = request.POST.get("bio")
		author.first_name = first_name
		author.last_name = last_name
		author.bio = bio

		author.save()

	return redirect('get_authors')

def delete_author(request, pk):
	author = get_object_or_404(Author, id = pk)
	author.delete()

	return redirect('get_authors')


def create_book(request):
	if request.method == "POST":
		title = request.POST.get("title")
		edition = request.POST.get("edition")
		pages = request.POST.get("pages")
		authors_ids = request.POST.getlist("authors") # [5, 10]
		publisher_id = request.POST.get('publisher')
		publisher = Publisher.objects.get(id = publisher_id)

		book = Book.objects.create(title = title, pages = pages, edition = edition, publisher = publisher)


		for author_id in authors_ids:
			author_obj = Author.objects.get(id = author_id)
			book.authors.add(author_obj)

		return redirect('books')
	else:
		authors = Author.objects.all()
		publishers = Publisher.objects.all()

		context = {'authors':authors, 'publishers':publishers}

		return render(request, 'create_book.html', context)

def get_books(request):
	books=Book.objects.all()
	context={'books': books}
	return render (request, 'books.html', context)

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = Author.objects.all()
    publishers = Publisher.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        edition = request.POST.get("edition")
        pages = request.POST.get("pages")
        publisher_id = request.POST.get("publisher")
        author_ids = request.POST.getlist("authors")  # To get multiple selected authors

        # Update the book instance
        book.title = title
        book.edition = edition
        book.pages = pages
        book.publisher = Publisher.objects.get(id=publisher_id)

        # Update the authors
        book.authors.set(Author.objects.filter(id__in=author_ids))  # This sets the new authors for the book

        book.save()

        return redirect('books')  # Redirect after saving

    return render(request, 'edit_book.html', {'book': book, 'authors': authors, 'publishers': publishers})

def delete_book(request,pk):
	book=get_object_or_404(Book, id=pk)
	book.delete()
	return redirect('books')


def create_publisher(request):
	if request.method=="POST":
		title=request.POST.get("title")
		country=request.POST.get("country")
		publisher=Publisher.objects.create(title=title, country=country)
		return HttpResponse(f"An object is created with an ID of {publisher.id}")
	else:
		return render(request, 'create_publisher.html')

def get_publishers(request):
	publisher=Publisher.objects.all()
	context={'publishers':publisher}
	return render(request,'publisher.html',context )

def edit_publisher(request, pk):
	publisher=get_object_or_404(Publisher, id = pk)
	if request.method == "GET":
		context = {'publisher': publisher}
		return render(request, 'edit_publisher.html', context)
	else :
		title=request.POST.get('title')
		country=request.POST.get('country')
		publisher.title=title
		publisher.country=country
		publisher.save()
		return redirect('get_publishers')
def delete_publisher(request,pk):
	publisher=get_object_or_404(Publisher,id=pk)
	publisher.delete()
	return redirect(get_publishers)
	

def greeting(request):
	return HttpResponse("Hello World.....!")

def message(request):
	return HttpResponse("welcom to my website")

def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')

def service(request):
	return render(request, 'services.html')

def edit(request, username):
	context = {'name': username}
	return render(request, 'response.html', context)

def form_submit(request):
	if request.method == 'POST':
		name = request.POST.get('uname')
		email = request.POST.get('email')
		password = request.POST.get('pass')

		context = {'name': name, 'email' : email}
		return render(request, 'response.html', context)



	return render(request, 'form.html')

def full_form(request):
	
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        dob = request.POST.get("dob")
        time = request.POST.get("time")
        interests = request.POST.getlist("interests")  # Multiple checkboxes
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        message = request.POST.get("message")
        file = request.FILES.get("file")

        # Process the data (For now, just returning a response)
        return HttpResponse(f"Received Data: {name}, {email}, {password}, {age}, {dob}, {time}, {interests}, {gender}, {country}, {message}, {file}")

    return render(request, "full_form.html")

def response(request):
	context = {'name': 'john doe', 'email':'john@gmail.com', 'age':25, 'intersts':['reading', 'sports', 'coding', 'writing', 'sleeping']}


	return render(request, 'response.html', context)
