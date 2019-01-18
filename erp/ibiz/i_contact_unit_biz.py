from erp.common.mapper import MapperType

class I_contact_unit_biz(metaclass=MapperType):
    def __init__(self, _instance):
        self.instance = _instance

from erp.common.mapper import Mapper
from erp.biz.contact_unit_biz import Contact_unit_biz
Mapper.register(I_contact_unit_biz, Contact_unit_biz)
