from django.urls import path
from .views import WalletListCreateAPIView

urlpatterns = [
    path('wallets/', WalletListCreateAPIView.as_view(), name='wallet-list-create'),
]
