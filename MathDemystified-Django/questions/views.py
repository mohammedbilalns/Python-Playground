from django.shortcuts import render

# Create your views here.

def questions_list(request):
        return render(request, 'questions_list.html')
