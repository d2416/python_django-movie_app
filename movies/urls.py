from django.urls import path
# from file views import function home_page
from .views import home_page

urlpatterns = [
  # url to access, use function home_page, reference name home_page 
  path('', home_page, name='home_page')
]