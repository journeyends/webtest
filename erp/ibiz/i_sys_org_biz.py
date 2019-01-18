from erp.common.mapper import MapperType, inject_biz


class I_sys_org_biz(metaclass=MapperType):
    def __init__(self, _instance):
        self.instance = _instance


inject_biz(I_sys_org_biz)
