from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    # this is my view
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context) #visit home page call index view and render tempalte index

def category_detail_view(request):
    category =  Category.objects.get(title='python')
    books = Book.objects.filter(category=category)

