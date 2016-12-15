from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class NCCTermParms(models.Model):
    name = models.CharField(max_length=32)
    tenant = models.ForeignKey(Group, on_delete=models.CASCADE)
    primaryNCCnumber = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Primary NCC number')
    alternateNCCnumber = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Alternate NCC number')
    CADId = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='CAD ID', blank=True, null=True)
    CPEId = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='CPE ID', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'tenant'),)
        verbose_name = 'NCC/terminal access parameters'
        verbose_name_plural = 'NCC/terminal access parameters'

