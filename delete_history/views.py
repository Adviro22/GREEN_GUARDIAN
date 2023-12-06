from django.shortcuts import render

# Create your views here.

def History(request):
    return render(request, 'historial.html')