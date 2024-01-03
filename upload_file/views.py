import os
import json
import datetime
import base64
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Registro

from show_result.models import Planta

def subida_archivos(request):
    #planta = Planta.objects.dates()
    return render(request, "uplaod_files.html")

@csrf_exempt
def save_result(request):
    try:
        if request.method == 'POST':
            # Obtener datos del cuerpo de la solicitud
            data = json.loads(request.body.decode('utf-8'))
            respuesta = data.get('respuesta', '')
            url_imagen = data.get('imagen', '')

            # Verificar que los valores no sean None
            if respuesta is not None and url_imagen is not None:
                # Obtener la fecha actual
                fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Guardar la imagen en la carpeta de archivos estáticos
                static_root = settings.STATIC_ROOT
                nombre_archivo = f'result_image_{fecha_actual}.jpg'
                ruta_archivo = os.path.join(static_root, 'ImagesResult', nombre_archivo)

                # Extraer la parte base64 del Blob URL
                _, base64_data = url_imagen.split(',')
                
                # Decodificar el Blob URL para obtener el archivo binario
                imagen_binaria = base64.b64decode(base64_data)

                with open(ruta_archivo, 'wb') as archivo:
                    archivo.write(imagen_binaria)

                # Crear un nuevo registro en la base de datos
                nuevo_registro = Registro(
                    fecha_registro=fecha_actual,
                    nom_imagen=nombre_archivo,
                    id_usuario=1 
                )
                nuevo_registro.save()

                # Devolver una respuesta JSON con la URL de la imagen
                url_imagen_completa = f'/static/ImagesResult/{nombre_archivo}'
                return JsonResponse({'mensaje': respuesta, 'url_imagen': url_imagen_completa})
            else:
                return JsonResponse({'mensaje': 'Datos faltantes en la solicitud'}, status=400)
        else:
            return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)