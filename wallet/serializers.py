from rest_framework import serializers
from .models import Transaction, Wallet


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = '__all__'

    def get_balance(self, obj):
        return obj.calculate_balance()


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
