from django.shortcuts import redirect
from django.template import loader
from p_library.models import Book, Publisher
from django.http import HttpResponse

def index(request):
	template = loader.get_template('index.html')
	books = Book.objects.all()
	# range_ = [x for x in range(1,100)]
	biblio_data = {"title": "мою библиотеку",
				 "books": books,
				#  "range_": range_,
				 }
	return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
	if request.method == 'POST':
		book_id = request.POST['id']
		if not book_id:
			return redirect('/index/')
		else:
			book = Book.objects.filter(id=book_id).first()
			if not book:
				return redirect('/index/')
			book.copy_count += 1
			book.save()
		return redirect('/index/')
	else:
		return redirect('/index/')

def book_decrement(request):
	if request.method == 'POST':
		book_id = request.POST['id']
		if not book_id:
			return redirect('/index/')
		else:
			book = Book.objects.filter(id=book_id).first()
			if not book:
				return redirect('/index/')
			if book.copy_count < 1:
				book.copy_count = 0
			else:
				book.copy_count -= 1
			book.save()
		return redirect('/index/')
	else:
		return redirect('/index/')

def publisher(request):
	template = loader.get_template('publisher.html')
	publishers = Publisher.objects.all()
	publishers_data = {"data": {publisher.name: 
						list(Book.objects.filter(publisher=publisher.id).values_list("title", flat=True))
						 for publisher in publishers}}
	return HttpResponse(template.render(publishers_data, request))


# Create your views here.
