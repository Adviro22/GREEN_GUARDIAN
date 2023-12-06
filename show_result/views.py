from django.shortcuts import render

# Create your views here.
def Show_Results(request):
    return render(request, 'resultados.html')
