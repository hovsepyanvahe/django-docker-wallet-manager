from django.db import models

class Wallet(models.Model):
    label = models.CharField(max_length=100)

    def calculate_balance(self):
        return sum(self.transaction_set.values_list('amount', flat=True))


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    txid = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
