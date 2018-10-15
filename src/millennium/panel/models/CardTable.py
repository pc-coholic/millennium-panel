from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from millennium.panel.framehelpers import mmByte, mmBCD, mmFlags

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

    def getFrame(self, MTRconfig):
        outframe = [0x16]

        for card in self.carddefs_set.all()[:(MTRconfig['DLOG_NUM_CARD_TYPES'] or MTRconfig['MAX_CARD_TABLE_ENTRIES'])]:
            outframe.extend(mmBCD(card.pan_low, 3))
            outframe.extend(mmBCD(card.pan_high, 3))
            outframe.extend(mmByte(card.standard_id))
            outframe.extend(mmFlags(card.control_inf))
            outframe.extend(mmByte(card.expiry_date_pos))
            outframe.extend(mmByte(card.initial_date_pos))
            outframe.extend(mmByte(card.discret_data_pos))

            # TODO: Selection if Magnetic or Smartcard
            #BCD                 service_code[10][2]; 10 * 3 BCD digits
        	#SCARD_SERVICE_CODE  smart_card;

            outframe.extend(mmByte(card.card_ref_num))
            outframe.extend(mmByte(card.carrier_id))

        # TODO: fill to MTRconfig['DLOG_NUM_CARD_TYPES'] or MTRconfig['MAX_CARD_TABLE_ENTRIES']

        return outframe

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'Card Table'
        verbose_name_plural = 'Card Tables'
