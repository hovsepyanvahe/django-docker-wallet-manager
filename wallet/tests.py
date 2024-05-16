from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase

from .models import Wallet, Transaction


class ModelCreationTestCase(TestCase):
    def test_wallet_creation(self):
        wallet = Wallet.objects.create(label='Test Wallet')
        self.assertEqual(wallet.label, 'Test Wallet')

    def test_transaction_creation(self):
        wallet = Wallet.objects.create(label='Test Wallet')
        tx = Transaction.objects.create(wallet=wallet, txid='tx1', amount=100)
        self.assertEqual(tx.wallet, wallet)
        self.assertEqual(tx.txid, 'tx1')
        self.assertEqual(tx.amount, 100)


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(label='Test Wallet')
        self.transaction = Transaction.objects.create(wallet=self.wallet, txid='tx1', amount=100)

    def test_wallet_list_endpoint(self):
        url = reverse('wallet-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['label'], 'Test Wallet')

    def test_transaction_list_endpoint(self):
        url = reverse('transaction-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['txid'], 'tx1')

    def test_wallet_create_endpoint(self):
        url = reverse('wallet-list-create')
        data = {'label': 'New Wallet'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 2)
        self.assertEqual(Wallet.objects.get(label='New Wallet').label, 'New Wallet')

    def test_transaction_create_endpoint(self):
        url = reverse('transaction-list-create')
        data = {'wallet': self.wallet.id, 'txid': 'tx2', 'amount': 200}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)
        self.assertEqual(Transaction.objects.get(txid='tx2').amount, 200)
