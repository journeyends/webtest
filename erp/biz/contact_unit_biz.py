from erp.idal.i_contact_unit_dal import I_contact_unit_dal


class Contact_unit_biz:
    dal = I_contact_unit_dal().instance()

    def getList(self, condition={}, user_info={}):
        dal = Contact_unit_biz.dal
        return dal.getList(condition=condition, user_info=user_info)
