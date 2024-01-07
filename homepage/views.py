from django.shortcuts import render

# Create your views here.

def Homepage(request):
    user_id = request.session.get('user_id', 0)
    return render(request, 'index.html', {'user_id': user_id})

def logout(request):
    try:
        del request.session['user_id']  # Eliminamos los datos de la session
        del request.session['user_correo']  # Eliminamos los datos de la session
        return render(request, 'index.html')
    except KeyError:
        return render(request, 'index.html')