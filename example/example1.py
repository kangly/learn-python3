"""
本地安装redis及'pip3 install redis'安装redis-py客户端后，输出国际惯例
Redis 5.0 或以上
redis-py 3.2.1 或以上
"""

from redis import Redis

# client = Redis()

# decode_responses=True 字符串解码
client = Redis(decode_responses=True)

# 设置缓存，60秒后自动过期
client.set('msg', 'hello world！', 60)

print(client.get('msg'))