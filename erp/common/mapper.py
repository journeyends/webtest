class Mapper(object):
    # 在字典里定义依赖注入关系
    __mapper_relation = {}

    # 类直接调用注册关系
    @staticmethod
    def register(cls, value):
        Mapper.__mapper_relation[cls] = value

    @staticmethod
    def exist(cls):
        if cls in Mapper.__mapper_relation:
            return True
        return False

    @staticmethod
    def get_value(cls):
        return Mapper.__mapper_relation[cls]


class MapperType(type):
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        arg_list = list(args)
        if Mapper.exist(cls):
            value = Mapper.get_value(cls)
            arg_list.append(value)
        obj.__init__(*arg_list, **kwargs)
        return obj


def inject_dal(idal, package_name="", file_name="", class_name=""):
    if package_name == "":
        package_name = "erp.dal"
    if file_name == "":
        file_name = idal.__name__
        if file_name.find('I_') == 0:
            file_name = file_name[2:]

    import importlib
    module = importlib.import_module(package_name + '.' + file_name)

    if class_name == "":
        class_name = idal.__name__[2:].capitalize()
    dal = getattr(module, class_name)

    Mapper.register(idal, dal)


def inject_biz(ibiz, package_name="", file_name="", class_name=""):
    if package_name == "":
        package_name = "erp.biz"
    if file_name == "":
        file_name = ibiz.__name__
        if file_name.find('I_') == 0:
            file_name = file_name[2:]

    import importlib
    module = importlib.import_module(package_name + '.' + file_name)

    if class_name == "":
        class_name = ibiz.__name__[2:].capitalize()
    biz = getattr(module, class_name)

    Mapper.register(ibiz, biz)
