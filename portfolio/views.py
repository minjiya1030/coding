from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')
def new(request):
    return render(request, 'portfolio/new.html')
