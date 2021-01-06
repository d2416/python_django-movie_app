from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# use Movie table database
from .models import Movie

def home_page(request):
  # get query to search in database
  user_query = str(request.GET.get('query', ''))
  # retrieve the existing movie(s) in Movie table
  # '__icontains' helps to get movies with part or entire user_query as name  
  search_result = Movie.objects.filter(name__icontains=user_query)
  # convert search_result to dictionary
  result = {"search_result": search_result}
  # modify movies/movie.html page in order to show the search result
  return render(request, 'movies/movies.html', result)