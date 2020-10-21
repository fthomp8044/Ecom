from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="3s9872fjbh7bd5rv",
        public_key="j5jw5p24fybzycp6",
        private_key="334253e1dcd578e7a9fe879b2d367573"
    )
)

def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = model.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return Falss

@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please login again!'})

    return JsonResponse({'ClientToken': gateway.client_token.generate(), 'success': True})
