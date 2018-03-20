from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

# Create your models here.

OnlyNumbersValidator = RegexValidator(
    r'^[0-9]*$',
    'Only 0-9 are allowed.',
    'Invalid Number'
)

ServiceCodeValidator = RegexValidator(
    r'^[125679][024][01234567]$',
    'Please enter a valid Service Code',
    'Invalid Service Code'
)

class CoinValTable(models.Model):
    name = models.CharField(
        max_length=32,
    )
    tenant = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    #coin_values[] -> CoinValDefs
    #coin_volumes[] -> CoinValDefs
    #coin_val_parms]] -> CoinValDefs
    cash_box_volume = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=20800,
        verbose_name='Cashbox Volume',
    )
    escrow_volume = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=600,
        verbose_name='Escrow Volume',
    )
    cash_box_volume_threshold = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=16640,
        verbose_name='Cashbox Volume Threshold',
    )
    cash_box_value_threshold = models.BigIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(4294967295),
            OnlyNumbersValidator
        ],
        default=25000,
        verbose_name='Cashbox Value Threshold',
    )
    escrow_volume_threshold = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=600,
        verbose_name='Escrow Volume Threshold',
    )
    escrow_value_threshold = models.BigIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(4294967295),
            OnlyNumbersValidator
        ],
        default=600,
        verbose_name='Escrow Value Threshold',
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'Coin Validator parameters'
        verbose_name_plural = 'Coin Validator parameters'
