from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.finance_request.api.serializers import ClientSerializer, RequestCreditSerializer
from apps.finance_request.models import Client, RequestCredit


# API Client
@api_view(['GET', 'POST'])
def client_api_view(request):

    # list
    if request.method == 'GET':

        # queryset
        clients_query = Client.objects.all()

        clients_serializer = ClientSerializer(clients_query, many=True)

        return Response({'results': clients_serializer.data}, status=status.HTTP_200_OK)

    # created
    elif request.method == 'POST':
        client_serializer = ClientSerializer(data=request.data)

        # validation
        if client_serializer.is_valid():
            client_serializer.save()
            return Response({'message': 'Cliente Creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail_view(request, pk=None):
    # queryset
    client = Client.objects.filter(id=pk).first()
    # validation
    if client:

        # retrieve
        if request.method == 'GET':
            client_serializer = ClientSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            client_serializer = ClientSerializer(client, data=request.data)

            # validation
            if client_serializer.is_valid():
                client_serializer.save()
                return Response({'results': client_serializer.data}, status=status.HTTP_200_OK)
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            client.delete()
            return Response({'message': 'Cliente Eliminado correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado un cliente con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def request_credit_api_view(request):

    # queryset
    requests_credits = RequestCredit.objects.all()
    # validation
    if requests_credits:

        # retrieve
        if request.method == 'GET':

            # queryset
            requests_credits_serializer = RequestCreditSerializer(requests_credits, many=True)
            return Response(requests_credits_serializer.data, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una Solicitud con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def request_credit_detail_view(request, pk=None):

    # queryset
    requests_credit = RequestCredit.objects.filter(id=pk).first()
    # validation
    if requests_credit:

        # retrieve
        if request.method == 'GET':
            requests_credit_serializer = RequestCreditSerializer(requests_credit)
            return Response(requests_credit_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            requests_credit_serializer = RequestCreditSerializer(requests_credit, data=request.data)

            # validation
            if requests_credit_serializer.is_valid():
                requests_credit_serializer.save()
                return Response({'results': requests_credit_serializer.data}, status=status.HTTP_200_OK)
            return Response(requests_credit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            requests_credit.delete()
            return Response({'message': 'Solicitud Eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una solicitud con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

