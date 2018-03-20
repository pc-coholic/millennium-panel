from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from .RateTable import RateTable

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

class RateDefs(models.Model):
    rateTable = models.ForeignKey(
        RateTable,
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField()
    rate_info = models.PositiveSmallIntegerField(
        choices=(
            ('0', 'NCC rated intralata'), # DLOG_RT_NCC_RATED_INTRA
            ('1', 'LMS rate - local'), # DLOG_RT_LMS_RATE
            ('2', 'Fixed charge - local'), # DLOG_RT_FIXED_CHARGE
            ('3', 'Rate not available'), # DLOG_RT_RATE_NA
            ('4', 'Invalid NPA/NXX'), # DLOG_RT_INV_NPA_NXX
            ('5', 'Toll intralata'), # DLOG_RT_TOLL_INTRALATA
            ('6', 'Toll interlata'), # DLOG_RT_TOLL_INTERLATA
            ('7', 'NCC rated interlata'), # DLOG_RT_NCC_RATED_INTER
            ('8', 'NCC rated local'), # DLOG_RT_NCC_RATED_LOCAL
            ('9', 'Toll international'), # DLOG_RT_TOLL_INTERNATIONAL, MTR2.x only
        ),
        null=True,
        blank=True,
        verbose_name='Rate Information',
        help_text='Toll international only available on MTR2.x'
    )
    initial_period = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        verbose_name='Initial period',
        help_text='0 equals indefinite duration'
    )
    initial_charge = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        verbose_name='Charge for initial period',
        help_text='in Cents'
    )
    additional_period = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        verbose_name='Additional period',
        help_text='0 equals indefinite duration'
    )
    additional_charge = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        verbose_name='Charge for every additional period',
        help_text='in Cents'
    )

    def __str__(self):
        return 'Rate ' + str(self.order)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Rate Definition'
        verbose_name_plural = 'Rate Definitions'
