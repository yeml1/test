import redis

class MyRedis(object):
    def __init__(self,host,password,port=6379):
        self.r=redis.Redis(host=host,password=password,port=port)
    def get(self,k):
        res=self.r.get(k)
        if res:
            res=res.decode()
         return res
    def set(self,k,v):
        self.r.set(k,v)
my_redis=MyRedis('116.196.122.221','123456')