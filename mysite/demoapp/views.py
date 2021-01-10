from django.shortcuts import render
from django.utils import timezone
from .models import Author, Book
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'list_authors':authors
    }
    return render(request, 'index.html', context)

def showBookOfAuthor(request):
    author_id = request.POST['id']
    author = Author.objects.get(pk=author_id)
    return render(request, 'showBookOfAuthor.html', {"authors":author})

def getFormLogin(request):
    return render(request, 'getFormLogin.html')

def postFormLogin(request):
    data_user = request.POST["user"]
    data_pass = request.POST["pass"]
    my_user = authenticate(username=data_user, password=data_pass)
    if not (my_user):
        return HttpResponse("User khong ton tai")
    return HttpResponse("Ban vua dang nhap thanh cong")