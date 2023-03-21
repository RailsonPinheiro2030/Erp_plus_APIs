from django.urls import path
from .views import StockView, StockViewAnalitics, History

urlpatterns = [
    path('', StockView.as_view(), name='estoque'),
    path('<int:pk>/', StockViewAnalitics.as_view(), name='analitics'),
    path('history/', History.as_view(), name='historico')
]