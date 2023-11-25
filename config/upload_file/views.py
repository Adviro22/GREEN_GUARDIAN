from django.shortcuts import render

# Create your views here.

def subida_archivos(request):
    return render(request, 'uplaod_files.htm')