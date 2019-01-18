from django.db import connection


def getPaginationListBySql(cursor=None, sqlListHead='',
                           sqlCountHead='', sqlCondition='',
                            orderName='id', orderDirection = 'asc',
                           pageIndex=0, pageSize=10):
    if cursor is None:
        cursor = connection.cursor()
    sqlList = sqlListHead + ' ' + sqlCondition + \
              ' order by {_order_name} {_order_direction}'\
              .format(_order_name=orderName, _order_direction=orderDirection) + \
              ' limit {_from},{_size}'.format(_from=str(pageIndex*pageSize), _size=str(pageSize))
    sqlCount = sqlCountHead + ' ' + sqlCondition
    values = getListBySql(cursor=cursor, sql=sqlList)
    count = getCountBySql(cursor=cursor, sql=sqlCount)
    return {'dataList': values, 'count': count}

def getListBySql(cursor=None, sql=''):
    if cursor is None:
        cursor = connection.cursor()
    cursor.execute(sql)
    values = dictfetchall(cursor)
    return values

def getCountBySql(cursor=None, sql=''):
    if cursor is None:
        cursor = connection.cursor()
    cursor.execute(sql, None)
    row = cursor.fetchone()
    count = row[0]
    return count

def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))for row in cursor.fetchall()]

class PaginationListModel:
    def getCursor(self):
        return None

    def getSqlListHead(self):
        return ''

    def getSqlCountHead(self):
        return ''

    def getSqlCondition(self):
        return ''

    def getOrderName(self):
        return 'id'

    def getOrderDirection(self):
        return 'asc'

    def getPageIndex(self):
        return 0

    def getPageSize(self):
        return 10

    def getPaginationListBySql(self):
        return getPaginationListBySql(sqlListHead=self.getSqlListHead(),
            sqlCountHead=self.getSqlCountHead(),
            sqlCondition=self.getSqlCondition(),
            orderName=self.getOrderName(),
            pageIndex=self.getPageIndex(),
            pageSize=self.getPageSize())
