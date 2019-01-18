from erp.common.mapper import MapperType, inject_dal


class I_sys_org_dal(metaclass=MapperType):
    def __init__(self, _instance):
        self.instance = _instance


inject_dal(I_sys_org_dal)
