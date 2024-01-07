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

@csrf_exempt
def save_result(request):
    try:
        if request.method == "POST":
            respuesta = request.POST.get("respuesta", "")
            cultivo = request.POST.get("cultivo", "")
            url_imagen = request.FILES.get('imagen')
            resultado = request.POST.get("resultado", "")
            print(resultado)

            if respuesta and cultivo and url_imagen:
                codigo_unico = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                nombre_archivo = f"result_image_{codigo_unico}.jpg"
                fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
                ruta_img = os.path.join(STATICFILES_DIRS[0], 'Img')

                if not os.path.exists(ruta_img):
                    os.makedirs(ruta_img)

                ruta_completa = os.path.join(ruta_img, nombre_archivo)

                with open(ruta_completa, 'wb') as img_file:
                    for chunk in url_imagen.chunks():
                        img_file.write(chunk)

                nuevo_registro = Registro(
                    fecha_registro=fecha_actual,
                    nom_imagen=nombre_archivo,
                    id_usuario=request.session.get("user_id", None),
                    plaga=respuesta,
                    cultivo=cultivo,
                    respuesta=resultado
                )
                nuevo_registro.save()

                url_imagen_completa = f"{STATICFILES_DIRS}Img/{nombre_archivo}"
                return JsonResponse(
                    {"mensaje": respuesta, "url_imagen": url_imagen_completa}
                )
            else:
                return JsonResponse(
                    {"mensaje": "Datos faltantes en la solicitud"}, status=400
                )
        else:
            return JsonResponse({"mensaje": "Método no permitido"}, status=405)
    except json.JSONDecodeError as e:
        return JsonResponse({"error": "Error de decodificación JSON"}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=500)