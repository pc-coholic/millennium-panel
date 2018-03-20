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

class NCCTermParms(models.Model):
    name = models.CharField(
        max_length=32,
    )
    tenant = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    # term_id
    datapac_num = models.CharField(
        max_length=12,
        validators=[
            OnlyNumbersValidator,
        ],
        default='15145551111',
        verbose_name='Primary NCC number',
        help_text='Pay attention to provide the right number. Entering the wrong number might involving a trip to your device to put it back in service!',
    )
    alt_datapac_num = models.CharField(
        max_length=12,
        validators=[
            OnlyNumbersValidator,
        ],
        default='15145551111',
        verbose_name='Alternate NCC number',
        help_text='If you do not have a secondary NCC access-number, put in the same as the primary one.',
    )
    cad_id = models.CharField(
        max_length=8,
        validators=[
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='CAD ID',
        help_text='MTR 2.x only',
    )
    cpe_id = models.CharField(
        max_length=8,
        validators=[
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='CPE ID',
        help_text='MTR 2.x only',
    )
    # spare[14] MTR 2.x only

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'NCC/terminal access parameters'
        verbose_name_plural = 'NCC/terminal access parameters'
