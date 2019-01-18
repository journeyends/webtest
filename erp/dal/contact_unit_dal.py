from erp.common.common_search import getListBySql, getCountBySql, getPaginationListBySql, PaginationListModel
from erp.entity.vw_sys_contact_unit import ContactUnit
import json

class Contact_unit_index_model(PaginationListModel):
    def __init__(self, _condition):
        self.condition = _condition

    def getSqlListHead(self):
        return 'select * '

    def getSqlCountHead(self):
        return 'select count(*)'

    def getSqlCondition(self):
        return 'from vw_sys_contact_unit'

    def getOrderName(self):
        return 'unit_id'

class Contact_unit_dal:
    def getListTest(self, condition={}, user_info={}):
        obj = ContactUnit.objects.all()[0:10].values('unit_id', 'unit_name')
        print(condition)
        print(user_info)
        datalist = json.dumps(list(obj), ensure_ascii=False)
        return datalist

    def getPaginationListTest(self, condition={}, user_info={}):
        sql = 'SELECT count(*) FROM vw_sys_contact_unit limit 5'
        return getPaginationListBySql(sqlListHead='select * ',
                                      sqlCountHead='select count(*)',
                                      sqlCondition='from vw_sys_contact_unit',
                                      orderName='unit_id',
                                      pageIndex=0, pageSize=6)

    def getList(self, condition={}, user_info={}):
        index_model = Contact_unit_index_model(condition).getPaginationListBySql()
        return index_model
