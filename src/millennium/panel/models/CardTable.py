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

            if card.service_code_1:
                # FIXME: empty servicecodes should be 0x00 0x00 and not 0x00 0x0E
                outframe.extend(mmBCD(card.service_code_1, 2, True))
                outframe.extend(mmBCD(card.service_code_2, 2, True))
                outframe.extend(mmBCD(card.service_code_3, 2, True))
                outframe.extend(mmBCD(card.service_code_4, 2, True))
                outframe.extend(mmBCD(card.service_code_5, 2, True))
                    # FIXME: output exactly SERVICE_CODE_SIZE / change model to FK for service CoinValDefs

                if MTRconfig['MTR'] is 1:
                    # FIXME: empty servicecodes should be 0x00 0x00 and not 0x00 0x0E
                    outframe.extend(mmBCD(card.service_code_6, 2, True))
                    outframe.extend(mmBCD(card.service_code_7, 2, True))
                    outframe.extend(mmBCD(card.service_code_8, 2, True))
                    outframe.extend(mmBCD(card.service_code_9, 2, True))
                    outframe.extend(mmBCD(card.service_code_10, 2, True))
                    # FIXME: output exactly SERVICE_CODE_SIZE / change model to FK for service CoinValDefs
                elif MTRconfig['MTR'] is 2:
                    outframe.extend(mmBCD(card.spill_string, MTRconfig['SPILL_STR_SIZE']))
                    outframe.extend(mmByte(card.spill_term_char))
                    outframe.extend(mmByte(card.disc_ptr))
            else:
                outframe.extend(mmByte(card.check_digit_1))
                outframe.extend(mmByte(card.check_digit_2))
                outframe.extend(mmByte(card.check_digit_3))
                outframe.extend(mmByte(card.check_digit_4))
                outframe.extend(mmByte(card.check_digit_5))
                outframe.extend(mmByte(card.check_digit_6))
                outframe.extend(mmByte(card.check_value_1))
                outframe.extend(mmByte(card.check_value_2))
                outframe.extend(mmByte(card.check_value_3))
                outframe.extend(mmByte(card.check_value_4))
                outframe.extend(mmByte(card.check_value_5))
                outframe.extend(mmByte(card.check_value_6))
                outframe.extend(mmByte(card.check_value_7))
                outframe.extend(mmByte(card.check_value_8))
                outframe.extend(mmByte(card.manufacturer_1))
                outframe.extend(mmByte(card.manufacturer_2))
                outframe.extend(mmByte(card.manufacturer_3))
                outframe.extend(mmByte(card.manufacturer_4))
                outframe.extend(mmByte(card.manufacturer_5))

                if MTRconfig['MTR'] is 1:
                    outframe.extend(mmByte(card.spare))
                elif MTRconfig['MTR'] is 2:
                    outframe.extend(mmByte(card.disc_ptr))

            outframe.extend(mmByte(card.card_ref_num))
            outframe.extend(mmByte(card.carrier_id))

            if MTRconfig['MTR'] is 2:
                outframe.extend(mmFlags(card.control_inf_1))
                outframe.extend(mmByte(card.bank_reload_ref))
                outframe.extend(mmByte(card.lang_code))

        # TODO: fill to MTRconfig['DLOG_NUM_CARD_TYPES'] or MTRconfig['MAX_CARD_TABLE_ENTRIES']

        return outframe

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'Card Table'
        verbose_name_plural = 'Card Tables'
