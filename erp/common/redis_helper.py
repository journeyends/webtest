import redis

def getRedisLink():
    r = redis.StrictRedis(host='172.21.204.62', port=6379, db=5, password='gmredis')
    return r
