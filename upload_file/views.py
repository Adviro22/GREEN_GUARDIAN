import os
import json
import datetime
import base64
import os.path
import urllib.request
from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse
from config.settings import STATICFILES_DIRS
from django.views.decorators.csrf import csrf_exempt
from .models import Registro
from show_result.models import Planta, Resultado
from django.http import HttpResponse


def subida_archivos(request):
    todas_las_plantas = Planta.objects.all()
    user_correo = request.session['correo']
    return render(
        request, "uplaod_files.html", {"todas_las_plantas": todas_las_plantas, 'correo': user_correo}
    )

def save_result(request):
    try:
        if request.method == "POST":
            # Obtener datos del cuerpo de la solicitud
            data = json.loads(request.body.decode("utf-8"))
            respuesta = data.get("respuesta", "")
            url_imagen = data.get("imagen", "")
            cultivo = data.get("cultivo", "")

            if respuesta:
                # Obtener la fecha actual
                fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
                nombre_archivo = f"result_image_{fecha_actual}.jpg"
                
                if STATICFILES_DIRS:
                    directorio_static = STATICFILES_DIRS[0]
                    ruta_img = os.path.join(directorio_static, 'Img')
                else:
                    print("STATICFILES_DIRS está vacío o no configurado correctamente.")

                # Ruta completa al archivo en static/Img
                ruta_completa = os.path.join(ruta_img, nombre_archivo)

                # Crear un nuevo registro en la base de datos
                nuevo_registro = Registro(
                    fecha_registro=fecha_actual,
                    nom_imagen=nombre_archivo,
                    imagen_binaria=bytes(url_imagen, 'utf-8'),  
                    id_usuario=request.session.get("user_id", None),
                    plaga=respuesta,
                    cultivo=cultivo
                )
                nuevo_registro.save()

                # Escribir el archivo binario
                with open(ruta_completa, 'wb') as img_file:
                    img_file.write(nuevo_registro.imagen_binaria)

                url_imagen_completa = f"/static/Img/{nombre_archivo}"
                return JsonResponse(
                    {"mensaje": respuesta, "url_imagen": url_imagen_completa}
                )
            else:
                print("Datos faltantes en la solicitud")
                return JsonResponse(
                    {"mensaje": "Datos faltantes en la solicitud"}, status=400
                )
        else:
            print("Método no permitido")
            return JsonResponse({"mensaje": "Método no permitido"}, status=405)
    except json.JSONDecodeError as e:
        print("Error de decodificación JSON:", str(e))
        return JsonResponse({"error": "Error de decodificación JSON"}, status=400)
    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)
