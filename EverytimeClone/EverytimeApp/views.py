from django.shortcuts import render, redirect
from .models import Board
from django.utils import timezone

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def main(request):
    return render(request, 'main.html')

# 자게 html
def freeBoard(request):
    return render(request, 'freeBoard.html')

def graduateBoard(request):
    return render(request, 'graduateBoard.html')

def create(request):
    if(request.method == 'POST'):
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.file = request.POST['file']
        post.date = timezone.now()
        post.save()
        return redirect('main')
    else:
        return render(request, 'freeBoard.html')