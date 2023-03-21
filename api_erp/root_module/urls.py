from django.urls import path, include
from .authentication import CustomAuth



urlpatterns = [
    path('auth/', CustomAuth.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', CustomAuth.as_view(), name='token_refresh'),
    path('estoque/', include('stock_module.urls')),
    
]

