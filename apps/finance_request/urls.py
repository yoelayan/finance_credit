from django.urls import path
from .views import (
    index_clients,
    change_approved,
    delete_request_credit,
)


urlpatterns = [
    path('', index_clients, name="client_index"),
    path('<int:pk>/change_approved/', change_approved, name='change_approved'),
    path('<int:pk>/delete/', delete_request_credit, name='delete_request_credit'),
]