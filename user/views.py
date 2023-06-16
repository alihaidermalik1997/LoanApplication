from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, SignUpSerializer, SignInSerializer, BlockUserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from LoanRESTAPI.permissions import IsManagerPermission
from rest_framework.generics import UpdateAPIView



class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer



class SignInView(APIView):
    serializer_class = SignInSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data['token'])


class ManageUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = BlockUserSerializer
    permission_classes = [IsManagerPermission]
    lookup_field = 'id'