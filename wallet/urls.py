from django.urls import path
from .views import WalletListCreateAPIView, TransactionListCreateAPIView

urlpatterns = [
    path('wallets/', WalletListCreateAPIView.as_view(), name='wallet-list-create'),
    path('transaction/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
]
