from django.urls import path
from .api import (
    client_api_view,
    client_detail_view,
    request_credit_detail_view,
    request_credit_api_view,
)


urlpatterns = [
    path('client/', client_api_view, name="client_api"),
    path('client/<int:pk>', client_detail_view, name="client_detail_api"),
    path('request/', request_credit_api_view, name="request_credit_detail_view"),
    path('request/<int:pk>', request_credit_detail_view, name="request_credit_api_view"),

]