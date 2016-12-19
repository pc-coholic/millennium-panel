from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

# Create your models here.

OnlyNumbersValidator =  RegexValidator(
    r'^[0-9]*$',
    'Only 0-9 are allowed.',
    'Invalid Number'
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

class FconfigOpts(models.Model):
    name = models.CharField(
        max_length=32,
    )
    tenant = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    terminal_type = models.PositiveSmallIntegerField(
        choices=(
            ('00', 'Unknwon Terminal Type'), # NULL_TERMINAL_TYPE
            ('01', 'Card Type Terminal'), # CARD_TERMINAL_TYPE
            ('02', 'Universal Type Terminal'), # UNIVERSAL_TERMINAL_TYPE
            ('03', 'Coin Terminal Type'), # COIN_TERMINAL_TYPE
            ('03', 'Maximim Terminal Type'), # MAXIMUM_TERMINAL_TYPE
            ('10', 'Smart Card Terminal Type'), # SMART_CARD_TERMINAL_TYPE
        ),
        default='02',
        verbose_name='Terminal Type',
    )
    display_present = models.BooleanField(
        default=True,
        verbose_name='Display present',
    )
    num_call_follow_on = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=5,
        null=True,
        blank=True,
        verbose_name='Number of Call follows',
    )
    card_validation_info = MultiSelectField(
        choices=(
            ('01', 'Auth for Local'), # DLOG_FCG_LOCAL_AUTH_REQ
            ('02', 'Delay Auth'), # DLOG_FCG_DELAY_AUTH
            ('04', 'MCE Auth for Local'), # DLOG_FCG_MCE_LOCAL_AUTH_REQ
            ('08', 'International'), # DLOG_FCG_VAL_INTL
            ('08', 'Insert NPA for 0+ Local/Intra'), # DLOG_FCG_INSERT_NPA_LOCAL
            ('10', 'Manually Entered Call Card'), # DLOG_FCG_MANUAL_CL_CARD
            ('00', 'ACCS Mode use NCC'), # DLOG_FCG_ACCS_MODE_NCC
            ('80', 'Validate after Number obtained'), # DLOG_FCG_MCE_VAL_AFTER_NUMBER
        ),
        default=['01', '04'],
        null=True,
        blank=True,
        verbose_name='Card validation info',
    )
    accs_info = MultiSelectField(
        choices=(
            ('01', 'ACCS Mode is available'), # DLOG_FCG_ACCS_AVAIL
            ('02', 'Route MCE Calls via 0+ network'), # DLOG_FCG_MCE_ROUTE_TO_ACCS
            ('04', 'MCE Feature enable'), # DLOG_FCG_ACCS_MCE_ENABLED
            ('08', 'MCE Calls MUST be NCC-validated'), # DLOG_FCG_ACCS_MCE_VAL_REQUIRED
            ('10', 'AOS Feature enable'), # DLOG_FCG_ACCS_AOS_ENABLED
            ('20', 'Strip off leading 0/1'), # DLOG_FCG_STRIP_OFF_0_OR_1
            ('80', 'Strip off local NPA'), # DLOG_FCG_STRIP_NPA_LOCAL
        ),
        default='01',
        null=True,
        blank=True,
        verbose_name='ACCS-Mode/Info',
    )
    incoming_call_mode = models.PositiveSmallIntegerField(
        choices=(
            ('0', 'Ringing disabled'), # RINGING_DISABLED
            ('1', 'Ringing / Incoming Voice'), # RINGING_INCOMING_VOICE
            ('2', 'No Ringing / Data Call'), # NO_RINGING_DATA_CALL
            ('3', 'Ringing / Voice / Delayed Data Call'), # RINGING_DELAYED_DATA_CALL
        ),
        default='1',
        verbose_name='Incoming Call mode',
    )
    incoming_call_anti_fraud = MultiSelectField(
        choices=(
            ('0', 'Answer Supervision'), # DLOG_FCG_ANS_SUPERVISN
        ),
        default='0',
        null=True,
        blank=True,
        verbose_name='Anti-Fraud for Incoming Call',
    )
    oos_pots_flags = MultiSelectField(
        choices=(
            ('01', 'Do not put Terminal Out-Of-Service when CDR list is full'), # CDR_FULL_NO_OOS
            ('02', 'Display Rate (MTR 1.x: Only Card-Terminals)'), # CARD_TERM_DISPLAY_RATE / TERM_DISPLAY_RATE
            ('04', 'INCOMMING_CALL_FCA_PRECED'), # INCOMMING_CALL_FCA_PRECED
            ('08', 'FCA_ZERO_VALUE_CARD'), # FCA_ZERO_VALUE_CARD
            ('10', 'MTR 1.x: Spare 4 / MTR 2.x: Automatically revert to primary Modem pool'), # SPARE_4 / REVERT_TO_PRIMARY_POOL
            ('20', 'MTR 1.x: Spare 5 / MTR 2.x: Block Carrier calls without nternal rate'), # SPARE_5 / BLOCK_NO_RATE_CARRIER
            ('40', 'MTR 1.x: Spare 6 / MTR 2.x: Creditcard CDRs should contain the charged amount for the calls'), # SPARE_6 / RATED_CREDIT_CARD_CDR
            ('80', 'MTR 1.x: Spare 7 / MTR 2.x: Force 11-digit-dialing on local calls'), # SPARE_7 / FORCE_11_DIGITS_LOCAL
        ),
        default=['01', '02', '04', '08'],
        null=True,
        blank=True,
        verbose_name='Out-Of-Service POTS Flags',
    )
    data_jack_visual_display = models.BooleanField(
        default=False,
        verbose_name='Datajack visual display',
    )

    incoming_call_rate = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=8,
        verbose_name='Incoming call rate',
        help_text='MTR1.x only'
    )
    language_scrolling_order = models.PositiveSmallIntegerField(
        choices=(
            ('1', 'English'), # LANGUAGE_1
            ('2', 'French'), # LANGUAGE_2
            ('3', 'Spanish'), # LANGUAGE_3
            ('4', 'Japanese'), # LANGUAGE_4
        ),
        default='1',
        verbose_name='Language Scrolling Order - 1st language',
        help_text='MTR 2.x only'
    )

    spareB = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Spare B',
        help_text='MTR1.x only'
    )
    language_scrolling_order_2 = models.PositiveSmallIntegerField(
        choices=(
            ('1', 'English'), # LANGUAGE_1
            ('2', 'French'), # LANGUAGE_2
            ('3', 'Spanish'), # LANGUAGE_3
            ('4', 'Japanese'), # LANGUAGE_4
        ),
        default='2',
        verbose_name='Language Scrolling Order - 2nd language',
        help_text='MTR 2.x only'
    )

    spareC = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Spare C',
        help_text='MTR1.x only'
    )
    number_of_languages = models.PositiveSmallIntegerField(
        choices=(
            ('1', '1 Language'),
            ('2', '2 Languages'),
            ('3', '3 Languages (MTR 2.x only)'),
            ('4', '4 Languages (MTR 2.x only)'),
        ),
        default='2',
        verbose_name='Number of Languages',
        help_text='MTR2.x only'
    )

    spareD = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Spare D',
        help_text='MTR1.x only'
    )
    rating_flags = MultiSelectField(
        choices=(
            ('01', 'Enable NPA SBR'), # NPA_SBR_ENABLE
            ('02', 'Enable International SBR'), # INTL_SBR_ENABLE
            #('03', ''), # INTL_SBR_FLAGS = (NPA_SBR_ENABLE|INTL_SBR_ENABLE)
            ('04', 'Enable Dial Around'), # DIAL_AROUND_ENABLED
            ('08', 'Show 1st xx min $, additional yy min $'), # SHOW_TIME_N_CHARGE
            ('10', 'Round up charge'), # SYSTEM_ROUND_UP
            ('20', '7-digit no-wait Option'), # SEVEN_DIGIT_NO_WAIT_ENABLE
        ),
        default=[],
        null=True,
        blank=True,
        verbose_name='Rating Flags',
        help_text='MTR2.x only'
    )

    spareE = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Spare E',
        help_text='MTR1.x only'
    )
    dial_around_timer = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Dial-around timer',
        help_text='MTR2.x only'
    )

    spareF = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Spare F',
        help_text='MTR1.x only'
    )
    opr_interntl_access_ptr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Pointer to international Access Operator',
        help_text='MTR2.x only'
    )

    aos_number = models.CharField(
        max_length=12,
        validators=[
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='AOS number',
        help_text='MTR 1.x only'
    )
    aos_interlata_access = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Pointer to Inter-LATA AOS-number',
        help_text='MTR2.x only'
    )
    aos_interntl_access = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Pointer to International Access AOS-number',
        help_text='MTR2.x only'
    )
    djack_grace_before_collect = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Datajack grace-periode before collection',
        help_text='MTR2.x only'
    )
    opr_collection_tmr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Operator collection timer	',
        help_text='MTR2.x only'
    )
    opr_intralata_access_ptr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Pointer to Intra-LATA operator access number',
        help_text='MTR2.x only'
    )
    opr_interlata_access_ptr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        null=True,
        blank=True,
        verbose_name='Pointer to Inter-LATA operator access number',
        help_text='MTR2.x only'
    )

    advert_enable = MultiSelectField(
        choices=(
            ('01', 'On Hook Adverts enabled'), # DLOG_FCG_ONHOOK_ADVERTS_ON
            ('02', 'Repdialer Adverts enabled'), # DLOG_FCG_REPDIALER_ADVERTS_ON
            ('04', 'Call Established adverts enabled'), # DLOG_FCG_CALL_EST_ADVERTS_ON
            #('06', 'Off Hook Adverts enabled'), # DLOG_FCG_OFFHOOK_ADVERTISING = (DLOG_FCG_REPDIALER_ADVERTS_ON | DLOG_FCG_CALL_EST_ADVERTS_ON)
            ('08', 'On Hook Date and Time displayed'), # DLOG_FCG_DATE_TIME_DISP_ON
            ('10', 'On Hook Date and Time displayed in 12hr Format'), # DLOG_FCG_DATE_TIME_DISP_12HR
        ),
        default=['01'],
        null=True,
        blank=True,
        verbose_name='Enable Advertising',
    )
    default_language = models.PositiveSmallIntegerField(
        choices=(
            ('1', 'English'), # LANGUAGE_1
            ('2', 'French'), # LANGUAGE_2
            ('3', 'Spanish'), # LANGUAGE_3
            ('4', 'Japanese'), # LANGUAGE_4
        ),
        default='1',
        verbose_name='Default Language',
    )

    display_called_number = MultiSelectField(
        choices=(
            ('01', 'Display Called Number Prompt'), # DLOG_FCG_DISPLAY_CALLED_NUM_PROMPT
            ('80', 'Surpress Calling Prompt'), # DLOG_FCG_SUPPRESS_CALLING_PROMPT
        ),
        default=['01'],
        null=True,
        blank=True,
        verbose_name='Called Number Displaying',
    )
    dtmf_duration = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=8,
        verbose_name='DTMF Duration',
    )
    inter_digit_pause = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=8,
        verbose_name='Inter-digit Pause',
    )

    dialing_conversion = MultiSelectField(
        choices=(
            ('01', 'Convert Operator to Toll'), # DLOG_FCG_DCV_OP_TO_TOLL
            ('02', 'Convert Toll to Operator'), # DLOG_FCG_DCV_TOLL_TO_OP
        ),
        default=['01', '02'],
        null=True,
        blank=True,
        verbose_name='Incoming Call mode',
        help_text='MTR 1.x only',
    )
    ppu_pre_auth_credit_limit = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='PPU PreAuth Credit Limit',
        help_text='MTR 2.x only',
    )

    coin_call_features = MultiSelectField(
        choices=(
            ('01', 'Overtime'), # DLOG_FCG_COIN_OVERTIME
            ('02', 'Voice-Feedback'), # DLOG_FCG_COIN_VFDBCK
            ('04', '2nd Warning'), # DLOG_FCG_COIN_2ND_WARN
        ),
        default=['02', '04'],
        null=True,
        blank=True,
        verbose_name='Coin calling Features',
    )
    coin_call_overtime_period = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=5,
        verbose_name='Coin call overtime period',
    )
    coin_call_pots_time = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=120,
        verbose_name='Coin call POTS time',
    )
    min_international_digits = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=5,
        verbose_name='Minimum number of digits for international calls',
    )
    def_rate_req_payment = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=10,
        verbose_name='default rate request payment type',
    )
    next_call_revalidation_freq = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Next Call re-validation frequency',
    )
    cutoff_on_disconnect_duration = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=45,
        verbose_name='Cutoff on disconnect duration',
    )
    cdr_upload_timer_int = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=0,
        verbose_name='CDR Upload timer for international calls',
    )
    cdr_upload_timer_nonint = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=0,
        verbose_name='CDR Upload timer for non-international calls',
    )
    perf_stats_dialog_fails = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Number of performance statistics dialog fails',
    )
    co_line_check_fails = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Number of CO-line-check fails',
    )
    alt_ncc_dialog_fails = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Number of alternative NCC-dialog-check fails',
    )
    dialog_fails_till_oos = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Number of failed dialogues until Terminal goes Out-Of-Service',
    )
    dialog_fails_till_alarm = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Number of failed dialogues until alarm is sent',
    )
    smart_card_flags = MultiSelectField(
        choices=(
            ('20', 'POST_PAYMENT_RATE_REQUEST'), # POST_PAYMENT_RATE_REQUEST
            ('80', 'DLOG_FCG_SUPPRESS_TERMINAL_RATE_INFO'), # DLOG_FCG_SUPPRESS_TERMINAL_RATE_INFO
        ),
        default=['01'],
        null=True,
        blank=True,
        verbose_name='Smartcard Flags',
    )
    max_man_card_dig = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=14,
        verbose_name='Maximum number of digits of manual card entry',
    )
    aos_intra_access_ptr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Pointer to Intra-AOS access-number',
    )
    carrier_reroute_flags = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Carrier reroute-flags',
    )
    min_man_card_dig = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=14,
        verbose_name='Minimum number of digits of manual card entry',
    )
    max_smart_card_inserts = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=5,
        verbose_name='Maximum number of smartcard-inserts',
    )
    max_diff_smart_card_inserts = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=5,
        verbose_name='Maximum number of different smartcard-inserts',
    )
    aos_operator_access_ptr = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Pointer to Operator AOS-number',
    )
    data_jack_flags = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Datajack-flag',
    )
    onhook_alarm_delay = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=500,
        verbose_name='Delay for on-hook card alarm delay',
    )
    post_onhook_alarm_delay = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=100,
        verbose_name='Delay for on-hook card alarm delay after call',
    )
    card_alarm_duration = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=1000,
        verbose_name='Duration of card-alarm',
    )
    alarm_cadence_on_timer = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=50,
        verbose_name='Card-alarm On-cadence',
    )
    alarm_cadence_off_timer = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=50,
        verbose_name='Card-alarm Off-cadence',
    )
    cardrdr_blocked_alarm_delay = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(65535),
            OnlyNumbersValidator
        ],
        default=300,
        verbose_name='Delay until card-reader blocked Alarm',
    )
    settle_time = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=8,
        verbose_name='Settlement time',
    )
    grace_period_domestic = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=5,
        verbose_name='Grace period for domestic calls',
    )
    ias_timeout = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=90,
        verbose_name='IAS timeout',
    )
    grace_period_international = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Grace period for international calls',
    )
    settle_time_datajack = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(255),
            OnlyNumbersValidator,
        ],
        default=0,
        verbose_name='Settlement-time for datajack-calls',
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'Feature Config & Call Options'
        verbose_name_plural = 'Feature Config & Call Options'
  
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
        verbose_name = 'Coin Validator Paramters'
        verbose_name_plural = 'Coin Validator Paramters'

class CoinValDefs(models.Model):
    coinValTable = models.ForeignKey(
        CoinValTable,
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

class CardTable(models.Model):
    name = models.CharField(
        max_length=32,
    )
    tenant = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'Card Table'
        verbose_name_plural = 'Card Tables'

class CardDefs(models.Model):
    cardTable = models.ForeignKey(
        CardTable,
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
            ('0', 'Not Set'), # DLOG_CTE_STDID_NOTSET 
            ('1', 'MOD10'), # DLOG_CTE_STDID_MOD10
            ('2', 'ANSI'), # DLOG_CTE_STDID_ANSI
            ('3', 'ABA'), # DLOG_CTE_STDID_ABA
            ('4', 'CBA'), # DLOG_CTE_STDID_CBA
            ('5', 'BOC'), # DLOG_CTE_STDID_BOC
            ('6', 'ANSI59'), # DLOG_CTE_STDID_ANSI59
            ('7', 'CCIT'), # DLOG_CTE_STDID_CCITT
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
            ('10', 'Early Card Specific Authorisation'), # EARLY_CARD_SPECIFIC_AUTH
            ('10', 'Delayed Card Specific Authorisation'), # DELAYED_CARD_SPECIFIC_AUTH
            ('20', 'Prompt for PIN'), # PROMPT_FOR_PIN
            ('40', 'Prompt for Telco PIN'), # PROMPT_FOR_TELCO_PIN
            ('80', 'Routing to ACCS'), # ROUTING_TO_ACCS
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
    #table_service_code
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
            ('10', 'Load-Only Magnetic Card'), # LOAD_ONLY_MAG_CARD
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
