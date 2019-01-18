from erp.common.mapper import MapperType

class I_contact_unit_dal(metaclass=MapperType):
    def __init__(self, _instance):
        self.instance = _instance

from erp.common.mapper import Mapper
from erp.dal.contact_unit_dal import Contact_unit_dal
Mapper.register(I_contact_unit_dal, Contact_unit_dal)
