from rest_framework import viewsets
from django.http import JsonResponse
# Manly responsible if the user is going to have a session token or not
from django.contrib.auth. import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt


# Valitdater if User is authenticated or not
def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        raise
