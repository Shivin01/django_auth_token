import json
from django.http import HttpResponse

from djangoauthtoken.models import TokenUser

def detail(request):
    token_users = TokenUser.objects.all()
    print(token_users)
    return HttpResponse("token users")