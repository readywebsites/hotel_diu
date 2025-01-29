from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Correct path without extra quotes
