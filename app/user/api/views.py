from rest_framework import generics, permissions
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication,\
                                            TokenAuthentication

from user.api.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manages the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
