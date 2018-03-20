from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from .CoinValTable import CoinValTable

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

class CoinValDefs(models.Model):
    coinValTable = models.ForeignKey(
        CoinValTable,
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField()
    coin_value = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=0,
        verbose_name='Coin Value',
    )
    coin_volume = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=0,
        verbose_name='Coin Volume',
    )
    coin_val_parms = MultiSelectField(
        choices=(
            ('01', 'Enable Coin Window'), # DLOG_CNVT_ENA_COIN_WIN
            ('02', 'Accept Coin'), # DLOG_CNVT_ACCEPT_COIN
        ),
        null=True,
        blank=True,
        verbose_name='Coin Parameters',
    )

    def __str__(self):
        return 'Coin ' + str(self.order)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Coin Validator Coin Definition'
        verbose_name_plural = 'Coin Validator Coin Definitions'        
