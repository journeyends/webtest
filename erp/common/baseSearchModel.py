class BaseSearchModel(object):
    def __init__(self):
        self._pageSize = 10
        self._pageIndex = 0
        pass

    @property
    def PageSize(self):
        if self._pageSize <= 0:
            self._pageSize = 10
        return self._pageSize

    @PageSize.setter
    def PageSize(self, value):
        self._pageSize = value

    @property
    def PageIndex(self):
        if self._pageIndex <= 0:
            self._pageIndex = 0
        return self._pageIndex

    @PageIndex.setter
    def PageIndex(self, value):
        self._pageIndex = value

    @property
    def OrderName(self):
        return self._orderName

    @OrderName.setter
    def OrderName(self, value):
        self._orderName = value

    @property
    def OrderDirection(self):
        return self._orderDirection

    @OrderDirection.setter
    def OrderDirection(self, value):
        self._orderDirection = value