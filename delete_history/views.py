from upload_file.models import Registro
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def History(request):
    try:
        user_id = request.session['user_id']
        user_correo = request.session['correo']
        user_records = Registro.objects.filter(id_usuario=user_id).order_by('-fecha_registro')
        return render(request, 'historial.html', {'user_records': user_records, 'correo': user_correo})
    except KeyError:
        return redirect('/loginusers/') 

def eliminar_registro(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    if request.method == 'POST':
        registro.delete()
        user_id = request.session['user_id']
        user_records = Registro.objects.filter(id_usuario=user_id).order_by('-fecha_registro')
        return render(request, 'historial.html', {'user_records': user_records})
    return ''

@csrf_exempt
def buscar_registros_por_rango_fecha(request):
    try:
        # Obtener los parámetros de fecha del request
        fecha_inicio_str = request.GET.get('fecha_inicio', '')
        fecha_fin_str = request.GET.get('fecha_fin', '')

        # Convertir las cadenas de fecha a objetos datetime si están presentes
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d') if fecha_inicio_str else None
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')  if fecha_fin_str else None

        # Obtener user_id y correo de la sesión
        user_id = request.session.get('user_id', None)
        user_correo = request.session.get('correo', None)

        # Verificar que user_id y correo estén presentes
        if user_id is None or user_correo is None:
            raise Exception("La sesión del usuario no contiene información completa.")
        print(f'Fecha Inicio:{fecha_inicio}')
        print(f'Fecha Fin: {fecha_fin}')
        # Filtrar registros por rango de fecha y user_id
        registros = Registro.objects.filter(
            id_usuario=user_id,
            fecha_registro__range=[fecha_inicio, fecha_fin]
        )

        print(registros)

        # Serializar los datos de los registros si es necesario
        # Puedes ajustar esta parte según tus necesidades y el formato de respuesta deseado

        # Por ejemplo, puedes devolver los datos en formato JSON
        data = [
                {
                    'id': registro.id,
                    'fecha_registro': registro.fecha_registro,
                    'nom_imagen': registro.nom_imagen,
                    'imagen_binaria': registro.imagen_binaria, 
                    'id_usuario': registro.id_usuario,
                    'plaga': registro.plaga,
                    'cultivo': registro.cultivo,
                    'resultado': registro.respuesta,
                    'eliminar': f" url 'eliminar_registro' {registro.id}  "
                }
    for registro in registros
]

        return JsonResponse({'registros': data})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)