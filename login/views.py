import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from register.models import user_register
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate



def login_view(request):
    return render(request, 'login.html')

@csrf_exempt
def login_user(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('email', '')
            password = data.get('password', '')

            # Obtener el usuario
            user = user_register.objects.get(user_name=username)
            # Verificar la contraseña
            if check_password(password, user.password):
                # Iniciar sesión si la autenticación es exitosa
                request.session['user_id'] = user.id
                response_data = {'message': 'Inicio de sesión exitoso'}
                print(response_data)
                return JsonResponse(response_data)
            else:
                response_data = {'error': 'Credenciales incorrectas'}
                print(response_data)
                return JsonResponse(response_data, status=401)
        else:
            return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)