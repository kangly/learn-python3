""" 使用 Redis 流实现的消息队列 """

from redis import Redis
from library.message_queue import MessageQueue

client = Redis(decode_responses=True)
mq = MessageQueue(client, 'mq')

for i in range(5):
    key = "key{0}".format(i)
    value = "value{0}".format(i)
    msg = {key: value}
    print(mq.add_message(msg))

print(mq.get_by_range('-', '+', 3))
