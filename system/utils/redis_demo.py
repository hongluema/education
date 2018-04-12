# encoding: utf-8
from redis import StrictRedis

def get_redis():
    rds = StrictRedis(host='localhost',port=6379,db=0)
    return rds

r = get_redis()

print "所有的keys:",r.keys()

print "所有key的类型(key, type(key)):",[(i,r.type(i)) for i in r.keys()]

print "*"*26+"string操作"+"*"*26

print "string的操作函数set:", r.set("sex","男",ex=16)
print "string的操作函数set:", r.mset({"sex":"男","hust":"华中大"})

print "string的操作函数get:", r.get("sex")
print "string的操作函数mget:", r.mget(["sex","hust"])

print "string的操作函数ttl:", r.ttl("sex")
print "string的操作函数append:", r.append("sex"," 女 或未知")
print "string的操作函数delete:", r.delete("sex")
print "string的操作函数getrange:", r.getrange("addr",0,-1)
print "string的操作函数strlen:", r.strlen("addr") #一个中文占3个字节

print "*"*26+"hash操作"+"*"*26

print "hash的操作函数hset:", r.hset("country","chinese","中国")
print "hash的操作函数hget:", r.hget("country","chinese")

print "hash的操作函数hmset:", r.hmset("province",{"center":"zhengzhou","north":"beijing","south":"shenzhen","west":"xian","east":"shanghai"})
print "hash的操作函数hgetall:", r.hgetall("province")
print "hash的操作函数hmget:", r.hmget("province",["center","south"])

print "hash的操作函数hlen:", r.hlen("province")
print "hash的操作函数hkeys:", r.hkeys("province")
print "hash的操作函数hvals:", r.hvals("province")

print "hash的操作函数hexists:", r.hexists("province","chengdu")
print "hash的操作函数hdel:", r.hdel("province","west")
print "hash的操作函数hkeys:", r.hkeys("province")

print "*"*26+"list操作"+"*"*26

print "list的操作函数lpush:", r.lpush("403",*["牛仪伟","董凯歌"])

print "list的操作函数lpop:", r.rpop("403")

print "list的操作函数llen:", r.llen("403")

print "list的操作函数linsert:", r.linsert("403","before","董凯歌","麻宏略")

print "list的操作函数lindex:", r.lindex("403",6)

print "list的操作函数lrange:", r.lrange("403",0,-1)
for i in r.lrange("403",0,-1):
    print i

print "*"*26+"set操作"+"*"*26

print "set的操作函数sadd:",r.sadd("city",*("项城","周口"))
print "set的操作函数smembers:",r.smembers("city") #获取city对应的集合的所有成员
print "set的操作函数scard:",r.scard("city") #city集合中的元素个数
print "set的操作函数smove:",r.srem("city",("项城","周口")) #删除city对应集合中的某些值
print "set的操作函数spop:",r.spop("city") #从city集合的右侧移除一个元素，并将其返回
print "set的操作函数smembers:",r.smembers("city")

print "*"*26+"有序集合操作"+"*"*26

print "有序集合的操作函数zadd:",r.zadd("friends","wang","yuan","chen")



