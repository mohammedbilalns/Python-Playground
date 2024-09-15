from django.shortcuts import render
from .models import Post

# Create your views here.

def notes_list(request):
        return render(request, 'notes_list.html')

def plusone(request):
        return render(request, 'plusone.html')

def plustwo(request):
        return render(request, 'plustwo.html')


def linearalgebra(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'linearalgebra.html', { 'posts': posts})

def notespage(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'notespage.html', { 'post': post})
