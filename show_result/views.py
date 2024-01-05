from django.shortcuts import render
from upload_file.models import Registro
# Create your views here.
def Show_Results(request):
    try:
        user_id = request.session['user_id']
        latest_record = Registro.objects.filter(id_usuario=user_id).latest('fecha_registro')
        print(latest_record.nom_imagen)  
        return render(request, 'resultados.html', {'latest_record': latest_record})
    except Registro.DoesNotExist:
        # Manejar la excepción si no hay registros para el usuario
        print("No se encontraron registros para el usuario.")
        return render(request, 'resultados.html', {'latest_record': None})