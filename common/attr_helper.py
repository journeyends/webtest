import time


def getTime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('运行时间：{_time}'.format(_time=end_time-start_time))
        return res
    return wrapper

def getTimeType(time_type='s'):
    def getTime(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            if time_type == 's':
                print('运行时间：{_time}'.format(_time=end_time-start_time))
            return res
        return wrapper
    return getTime
