# 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import redis

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# r.set('name', 'junxi')
# print(r['name'])
# print(r.get('name'))
# print(type(r.get('name')))

# r.sadd("articlesTitle", 'aa')  # 往集合中添加元素
# print(r.scard("set1"))  # 集合的长度是4
# print(r.smembers("set1"))   # 获取集合中所有的成员
# r.sadd("articlesTitle", 'aa')
# print( not  (r.sismember("articlesTitle", '面试回答问题的技巧：求职面试时的自杀式回答')))  # 33是集合的成员
# print(r.sismember("set1", 23))  # 23不是集合的成员
# r.s("ID",1)
# print(r.sismember("ID",1))
r.hset('hash1','id',1)
# r.hincrby('hash1', 'id', amount=1)
# print(r.hget('hash1','id'))

print(type(r.hget('hash1', 'id')))
