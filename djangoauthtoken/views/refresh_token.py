from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from djangoauthtoken.models import TokenUser, Token

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def refresh_token(request):
    """
    Refresh Token request.
    """
    try:
        data = request.data
        token = data['token']
        refresh_token = data['refresh_token']
        user_id = data['user_id']

        user = TokenUser.objects.get(id=user_id)
        user_token = Token.objects.get(user=user, token=token, refresh_token=refresh_token)

        token = Token(user=user)
        token.save()

        return Response({
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "token": user_token.token,
                    "refresh_token": user_token.refresh_token,
                    "expires_at": user_token.expiry_time
                    },
                    status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

