from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from .CardTable import CardTable

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

class CardDefs(models.Model):
    cardTable = models.ForeignKey(
        CardTable,
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField()
    pan_low = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(999999),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Start of PAN-Range',
        help_text='First six digits of card',
    )
    pan_high = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(999999),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='End of PAN-Range',
        help_text='First six digits of card',
    )
    standard_id = models.PositiveSmallIntegerField(
        choices=(
            (0, 'Not Set'), # DLOG_CTE_STDID_NOTSET
            (1, 'MOD10'), # DLOG_CTE_STDID_MOD10
            (2, 'ANSI'), # DLOG_CTE_STDID_ANSI
            (3, 'ABA'), # DLOG_CTE_STDID_ABA
            (4, 'CBA'), # DLOG_CTE_STDID_CBA
            (5, 'BOC'), # DLOG_CTE_STDID_BOC
            (6, 'ANSI59'), # DLOG_CTE_STDID_ANSI59
            (7, 'CCIT'), # DLOG_CTE_STDID_CCITT
            (8, 'PINOFF'), # DB Design Guide
            (9, 'HELLO'), # DB Design Guide
            (10, 'SMART CARD'), # DB Design Guide
            (11, 'Reserved'), # DB Design Guide
            (12, 'SmartCity GPM416'), # DB Design Guide
            (13, 'SMARTCITY PCOS'), # DB Design Guide
            (14, 'SMARTCITY MPCOS'), # DB Design Guide
            (15, 'PROTON'), # DB Design Guide
        ),
        null=True,
        blank=True,
        verbose_name='Card Verification Standard',
    )
    control_inf = MultiSelectField(
        choices=(
            ('01', 'Formatted Request'), # FORMATTED_REQUEST
            ('01', 'Unformatted Request'), # UNFORMATTED_REQUEST
            ('02', 'Positive Validation'), # POSITIVE_VALIDATION
            ('04', 'NCC Validation Required'), # NCC_VALIDATION_REQUIRED
            ('08', 'Calling card'), # CALLING_CARD
            ('08', 'Not a calling card'), # NOT_CALLING_CARD
            ('16', 'Early Card Specific Authorisation'), # EARLY_CARD_SPECIFIC_AUTH
            ('16', 'Delayed Card Specific Authorisation'), # DELAYED_CARD_SPECIFIC_AUTH
            ('32', 'Prompt for PIN'), # PROMPT_FOR_PIN
            ('64', 'Prompt for Telco PIN'), # PROMPT_FOR_TELCO_PIN
            ('128', 'Routing to ACCS'), # ROUTING_TO_ACCS
        ),
        null=True,
        blank=True,
        verbose_name='Control Information Flags',
    )
    expiry_date_pos = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Position of Expiry Date',
        help_text='Relative to 1st Field Separator',
    )
    initial_date_pos = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Position of Issue Date',
        help_text='Relative to 1st Field Separator',
    )
    discret_data_pos = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Position of Discretionary Data',
        help_text='Relative to 1st Field Separator',
    )
    service_code_1 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='1st 3 Digit Service Code',
        help_text='Magnetic Stripe Cards only',
    )
    service_code_2 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='2nd 3 Digit Service Code',
        help_text='Magnetic Stripe Cards only',
    )
    service_code_3 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='3rd 3 Digit Service Code',
        help_text='Magnetic Stripe Cards only',
    )
    service_code_4 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='4th 3 Digit Service Code',
        help_text='Magnetic Stripe Cards only',
    )
    service_code_5 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='5th 3 Digit Service Code',
        help_text='Magnetic Stripe Cards only',
    )
    service_code_6 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='6th 3 Digit Service Code',
        help_text='MTR 1.x only. Magnetic Stripe Cards only',
    )
    service_code_7 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='7th 3 Digit Service Code',
        help_text='MTR 1.x only. Magnetic Stripe Cards only',
    )
    service_code_8 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='8th 3 Digit Service Code',
        help_text='MTR 1.x only. Magnetic Stripe Cards only',
    )
    service_code_9 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='9th 3 Digit Service Code',
        help_text='MTR 1.x only. Magnetic Stripe Cards only',
    )
    service_code_10 = models.PositiveSmallIntegerField(
        validators=[
            ServiceCodeValidator,
        ],
        null=True,
        blank=True,
        verbose_name='10th 3 Digit Service Code',
        help_text='MTR 1.x only. Magnetic Stripe Cards only',
    )
    spill_string = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name='Spill String',
        help_text='MTR 2.x only. Magnetic Stripe Cards only',
    )
    spill_term_char = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name='Terminating Character for Spill String',
        help_text='MTR 2.x only. Magnetic Stripe Cards only',
    )
    disc_ptr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Index for discounted rate in smartcard-table',
        help_text='MTR 2.x only. Magnetic Stripe Cards only',
    )
    check_digit_1 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='1st Check Digit',
        help_text='Smartcard only',
    )
    check_digit_2 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='2nd Check Digit',
        help_text='Smartcard only',
    )
    check_digit_3 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='3rd Check Digit',
        help_text='Smartcard only',
    )
    check_digit_4 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='4th Check Digit',
        help_text='Smartcard only',
    )
    check_digit_5 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='5th Check Digit',
        help_text='Smartcard only',
    )
    check_digit_6 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='6th Check Digit',
        help_text='Smartcard only',
    )
    check_value_1 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='1st Check Value',
        help_text='Smartcard only',
    )
    check_value_2 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='2nd Check Value',
        help_text='Smartcard only',
    )
    check_value_3 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='3rd Check Value',
        help_text='Smartcard only',
    )
    check_value_4 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='4th Check Value',
        help_text='Smartcard only',
    )
    check_value_5 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='5th Check Value',
        help_text='Smartcard only',
    )
    check_value_6 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='6th Check Value',
        help_text='Smartcard only',
    )
    check_value_7 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='7th Check Value',
        help_text='Smartcard only',
    )
    check_value_8 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='8th Check Value',
        help_text='Smartcard only',
    )
    manufacturer_1 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='1st Manufacturer Value',
        help_text='Smartcard only',
    )
    manufacturer_2 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='2nd Manufacturer Value',
        help_text='Smartcard only',
    )
    manufacturer_3 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='3rd Manufacturer Value',
        help_text='Smartcard only',
    )
    manufacturer_4 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='4th Manufacturer Value',
        help_text='Smartcard only',
    )
    manufacturer_5 = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='5th Manufacturer Value',
        help_text='Smartcard only',
    )
    spare = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='MTR 1.x: Spare / MTR 2.x: Index for discounted rate in smartcard-table',
        help_text='MTR1.x only'
    )
    card_ref_num = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Position of Language',
        help_text='Relative to 1st Field Separator',
    )
    carrier_id = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Carrier ID',
    )
    control_inf_1 = MultiSelectField(
        choices=(
            ('02', 'Reloadable Smart Card'), # RELOADABLE_SMART_CARD
            ('04', 'SUMMARY_CARD_REQUIRED'), # SUMMARY_CARD_REQUIRED
            ('08', 'Display remaining Credit'), # DISPLAY_CREDIT_REMAINING
            ('16', 'Load-Only Magnetic Card'), # LOAD_ONLY_MAG_CARD
        ),
        null=True,
        blank=True,
        verbose_name='Control Information Flags',
        help_text='MTR 2.x only',
    )
    bank_reload_ref = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Bank Reload Reference',
        help_text='MTR 2.x only',
    )
    lang_code = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='language code to spill to switch',
        help_text='MTR 2.x only',
    )

    def __str__(self):
        return 'Card ' + str(self.order)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Card Definition'
        verbose_name_plural = 'Card Definitions'
