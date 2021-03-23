from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.users.api.urls')),
    path('api/v1/', include('apps.finance_request.api.urls')),
    path('client/', include('apps.finance_request.urls')),
    path('', include('apps.base.urls')),
]
