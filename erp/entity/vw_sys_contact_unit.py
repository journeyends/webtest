from django.db import models
from rest_framework import serializers

from erp.common.baseSearchModel import BaseSearchModel


class ContactUnit(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "vw_sys_contact_unit"

class ContactUnitIndexModel:
    pass

class ContactUnitSearchModel(BaseSearchModel):
    @property
    def UnitName(self):
        return self._unitName

    @UnitName.setter
    def UnitName(self, value):
        self._unitName = value

class ContactUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUnit
        fields = ('unit_id', 'unit_name')
