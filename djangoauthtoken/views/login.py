from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from djangoauthtoken.models import TokenUser

@csrf_exempt
@api_view(["POST"])
def login(request):
    """
    Login view
    It expects username and password.
    #TODO: Flag to switch to Email.
    """
    data = request.data
    print(data)
    username = data['username']
    password = data['password']
    try:
        if _auth := auth.authenticate(username=username, password=password):
            # create a token object.
            # create a csrf token and assign that.
            # return user details.
            print('AUTH')
            print(_auth)
            token = True
            user = TokenUser.objects.get(username=username)
            print(user)
            return Response({
                "message": "need to update this",
                }, status=status.HTTP_200_OK)
        else:
            # Create your own Exception layer.
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

