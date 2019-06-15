# 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import redis

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# r.set('name', 'junxi')
# print(r['name'])
# print(r.get('name'))
# print(type(r.get('name')))

r.sadd("articlesTitle", 0)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))   # 获取集合中所有的成员
r.sadd("articlesTitle", '啦啦啦')
print(r.sismember("articlesTitle", '啦啦啦'))  # 33是集合的成员
print(r.sismember("set1", 23))  # 23不是集合的成员