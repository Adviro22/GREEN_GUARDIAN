
from upload_file.models import Registro
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def History(request):
    user_id = request.session['user_id']
    user_correo = request.session['correo']
    user_records = Registro.objects.filter(id_usuario=user_id).order_by('-fecha_registro')
    return render(request, 'historial.html', {'user_records': user_records, 'correo': user_correo})

def eliminar_registro(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    if request.method == 'POST':
        registro.delete()
        user_id = request.session['user_id']
        user_records = Registro.objects.filter(id_usuario=user_id).order_by('-fecha_registro')
        return render(request, 'historial.html', {'user_records': user_records})
    return ''