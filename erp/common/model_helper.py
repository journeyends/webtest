from erp.common.datetime_helper import getDatetimeNowStr


def initEntityData(obj, request=None):
    if hasattr(obj, "is_del"):
        obj.is_del = 0
    if hasattr(obj, "is_post"):
        obj.is_post = 0
    if hasattr(obj, "check_status"):
        obj.check_status = 0
    if hasattr(obj, "create_user_id") and request is not None and hasattr(obj, "current_user_id"):
        obj.create_user_id = request.current_user_id
    else:
        obj.create_user_id = 0
    if hasattr(obj, "create_date"):
        obj.create_date = getDatetimeNowStr()
