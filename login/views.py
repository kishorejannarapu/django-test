from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .auth import LdapAuthentication


@api_view(['POST'])
@authentication_classes([LdapAuthentication])
# @permission_classes([])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Generate and return JWT token
        from rest_framework_jwt.settings import jwt_encode_handler
        token = jwt_encode_handler(user)
        return Response({'token': token})
    return Response({'error': 'Invalid credentials'}, status=401)

# @api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def protected_data(request):
#     # Access user information from LDAP here
#     # based on username or other LDAP attributes
#     user_data = ...
#     return Response(user_data)
