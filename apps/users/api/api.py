from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer
from apps.users.models import User


@api_view(['GET', 'POST'])
def user_api_view(request):

    # list
    if request.method == 'GET':

        # queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # created
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        # validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario Creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    # queryset
    user = User.objects.filter(id=pk).first()
    # validation
    if user:

        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data, status=status.HTTP_200_OK)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Usuario Eliminado correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


""" 
Api Basado en Class
class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
"""
