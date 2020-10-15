from rest_framework import viewsets
from rest_framework.permission import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
# importtant vvv
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout

import random
# for regular expressions
import re

def generate_session_token(length=10):
    # generates a string thats 10 characters long
    return ''.join(random.SystemRandom().choice([char(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))
    
@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameter only'})

    username = request.POST['email']
    password = request.POST['password']

    # validaton part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'errorr': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at least of 3 char'})

    UserModel = ger_user_model()

    try:
        user = UserModel.objects.get(email=username)
        # match password of the user vvv
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': 'Previous session exists!'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})


    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})
