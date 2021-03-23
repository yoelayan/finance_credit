from rest_framework import serializers
from apps.finance_request.models import Client, RequestCredit


class RequestCreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestCredit
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    requests_credits = RequestCreditSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
