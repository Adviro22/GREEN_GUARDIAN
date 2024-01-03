import json
from django.shortcuts import render
from .models import user_register
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def register(request):
    return render(request, 'Register.html')

@csrf_exempt
def create_register(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            print(f'/***/ {data} /***/')
            name = data.get('name', '')
            e_mail = data.get('email', '')
            password = data.get('password', '')

            user = user_register.objects.filter(user_name=e_mail).first()
            if(user):
                return JsonResponse({'mensaje': 'El usuario ya esta creado'}, status=405)
            # Crear el nuevo registro
            nuevo_registro = user_register(
                name=name,
                user_name=e_mail,
                e_mail=e_mail,
                password=password
            )
            nuevo_registro.save()

            # Devolver una respuesta exitosa
            response_data = {'message': 'Registro exitoso'}
            
            return JsonResponse(response_data)
        else:
            return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    except Exception as e:
        # Imprimir el traceback para obtener más información sobre la excepción
        import traceback
        traceback.print_exc()

        # Devolver una respuesta de error
        return JsonResponse({'error': str(e)}, status=500)
