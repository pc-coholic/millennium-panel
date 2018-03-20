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

class InstallParms(models.Model):
    name = models.CharField(
        max_length=32,
    )
    tenant = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    access_code = models.CharField(
        max_length=7,
        validators=[
            MinLengthValidator(7),
            OnlyNumbersValidator,
        ],
        default='2727378',
        verbose_name='Craft-interface access code',
        help_text='For default access-code CRASERV: 2727378',
    )
    key_card_num = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10),
            OnlyNumbersValidator,
        ],
        default='0000000000',
        verbose_name='Craft-interface keycard number',
        help_text='Only for DeskSets. Keep 0000000000 for MultiPay devices.',
    )
    install_servicing_flags = MultiSelectField(
        choices=(
            ('01', 'Predial string enable'), # PREDIAL_STRING_ENABLE
            ('02', 'Predial string enable for toll 1+ calls'), # PREST_TOLL_ENABLE
            ('04', 'Predial string enable for intl 011+ calls'), # PREST_INTL_ENABLE
            ('08', 'Prefix prdial string to all except free calls'), # PREST_ALL_EXCEP_FREE
            ('10', 'MTR 1.x: Spare 4 / MTR 2.x: Predial string enable for primary datapac'), # SPARE_4 / PDS_PRIMARY_DP_NUM
            ('20', 'MTR 1.x: Spare 5 / MTR 2.x: Predial string enable for alternate datapac'), # SPARE_5 / PDS_ALTERNATE_DP_NUM
            ('40', 'MTR 1.x: Spare 6 / MTR 2.x: AMP enable'), # SPARE_6 / ANALOG_MODE_PREFIX_ENABLE
            ('80', 'Spare 7'), # SPARE_7
        ),
        null=True,
        blank=True,
        verbose_name='Install/Servicing Flags',
    )
    tx_pkt_delay = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=10,
        verbose_name='TX Paket Delay',
    )
    rx_pkt_gap = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=10,
        verbose_name='RX Paket Gap',
    )
    retries_till_oos = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=40,
        verbose_name='Retries until Out-Of-Service',
    )
    coin_servicing = MultiSelectField(
        choices=(
            ('02', 'Cashbox Query Menu is Accessible'), # CASHBOX_QUERY_ENABLE
        ),
        null=True,
        blank=True,
        verbose_name='Coin servicing flags',
        help_text='MTR 2.x only',
    )
    coin_box_lock_timeout = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=300,
        verbose_name='Coinbox Lock Timeout',
    )
    predial_string = models.CharField(
        max_length=8,
        validators=[
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Predial String',
    )
    alt_predial_string = models.CharField(
        max_length=8,
        validators=[
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Alternate Predial String',
    )

    # Spare for MTR1.x
    analog_mode_prefix = models.CharField(
        max_length=12,
        validators=[
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Analog mode prefix for datacalls using wireless setup',
        help_text='MTR 2.x only',
    )
    comm_saving_flags = MultiSelectField(
        choices=(
            ('01', 'Store OP-Code 996 to Upload Later with Call-in'), # OPCODE_996_UPLOAD_DELAY
        ),
        null=True,
        blank=True,
        verbose_name='Communication saving flags',
        help_text='MTR 2.x only',
    )
    retries_till_oos = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Voice data timeout',
        help_text='MTR 2.x only',
    )
    ds_serv_enable_flags = MultiSelectField(
        choices=(
            ('01', 'Enable CS-Serv - probably...'),
        ),
        null=True,
        blank=True,
        verbose_name='DS Serv enable flags',
        help_text='MTR 2.x only',
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'Installation/Service parameters'
        verbose_name_plural = 'Installation/Service parameters'
