from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Santiago Henao'})

def about(request):
    return HttpResponse('About Page')