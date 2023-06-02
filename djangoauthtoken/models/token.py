from django.db import models
from django.conf import settings

from djangoauthtoken.models import Base, TokenUser

class Token(Base):

    token = models.CharField(max_length=Base.MAX_LENGTH_SMALL)
    refresh_token = models.CharField(max_length=Base.MAX_LENGTH_SMALL)
    expiry_time = models.IntegerField(default=settings.EXPIRY)
    user = models.ForeignKey(TokenUser, on_delete=models.CASCADE)
