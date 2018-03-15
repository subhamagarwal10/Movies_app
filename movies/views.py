from django.shortcuts import render, redirect
from . models import movies
# Create your views here.
def index(request):
	user_query = request.GET.get('movie_name')
	if user_query:
		response = movies.objects.all().filter(Name__icontains=user_query)
	else:
		response = movies.objects.all()
	stuff_for_frontend = {'response':response}
	return render(request, 'movies/movies_stuff.html', stuff_for_frontend)
	
def create(request):
	if request.method == "POST":
		data={
			'Name':request.POST.get('name'),
			'Picture':request.POST.get('url'),
			'Rating':int(request.POST.get('rating')),
			'Notes':request.POST.get('review'),
		}	
		
		response = movies.objects.create(**data)		
	return redirect("/")
	
def update(request, movie_id):
	if request.method == "POST":
		print(movie_id)
		response = movies.objects.filter(id=movie_id)
		data={
			'Name':request.POST.get('name'),
			'Picture':request.POST.get('url'),
			'Rating':int(request.POST.get('rating')),
			'Notes':request.POST.get('review'),
		}	
		
		response.update(**data)	
	return redirect("/")
	
def delete(request, movie_id):
	response = movies.objects.filter(id=movie_id)
	response.delete()
	return redirect("/")