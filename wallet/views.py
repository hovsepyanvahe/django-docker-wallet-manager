from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Transaction, Wallet
from .serializers import TransactionSerializer, WalletSerializer


class WalletListCreateAPIView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['label']


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['wallet', 'txid', 'amount']
