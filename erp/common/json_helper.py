def bindModelByJson(objType, jsonDic, objTypeName=""):
    if objTypeName == "":
        objTypeName = objType._meta.db_table
    obj = objType()
    jsonObj = jsonDic.get(objTypeName)

    if jsonObj is None:
        return obj

    for f in objType._meta.fields:
        setattr(obj, f.name, jsonObj.get(f.name))

    return obj

