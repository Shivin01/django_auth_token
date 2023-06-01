import json
from django.http import HttpResponse
from rest_framework import viewsets

from djangoauthtoken.models import TokenUser
from djangoauthtoken.serializers import UserSerializer

def detail(request):
    token_users = TokenUser.objects.all()
    print(token_users)
    return HttpResponse("token users")

class UserViewSet(viewsets.ModelViewSet):
    queryset = TokenUser.objects.all()
    serializer_class = UserSerializer
