from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from .NCCTermParms import NCCTermParms
from .InstallParms import InstallParms
from .FconfigOpts import FconfigOpts
from .CoinValTable import CoinValTable
from .CardTable import CardTable
from .RateTable import RateTable
from .NPANXXTable import NPANXXTable
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

class terminal(models.Model):
    term_id = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10),
            OnlyNumbersValidator,
        ],
        verbose_name='Terminal ID',
        help_text='aka: the phone\'s number',
    )
    tenant = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    NCCTermParms = models.ForeignKey(
        NCCTermParms,
        on_delete=models.CASCADE,
        verbose_name=NCCTermParms._meta.verbose_name_raw
    )
    InstallParms = models.ForeignKey(
        InstallParms,
        on_delete=models.CASCADE,
        verbose_name=InstallParms._meta.verbose_name_raw
    )
    FconfigOpts = models.ForeignKey(
        FconfigOpts,
        on_delete=models.CASCADE,
        verbose_name=FconfigOpts._meta.verbose_name_raw
    )
    CoinValTable = models.ForeignKey(
        CoinValTable,
        on_delete=models.CASCADE,
        verbose_name=CoinValTable._meta.verbose_name_raw
    )
    CardTable = models.ForeignKey(
        CardTable,
        on_delete=models.CASCADE,
        verbose_name=CardTable._meta.verbose_name_raw
    )
    RateTable = models.ForeignKey(
        RateTable,
        on_delete=models.CASCADE,
        verbose_name=RateTable._meta.verbose_name_raw
    )
    NPANXXTable = models.ForeignKey(
        NPANXXTable,
        on_delete=models.CASCADE,
        verbose_name=NPANXXTable._meta.verbose_name_raw
    )

    def __str__(self):
        return self.term_id

    class Meta:
        verbose_name = 'Terminal configuration'
        verbose_name_plural = 'Terminal configurations'
