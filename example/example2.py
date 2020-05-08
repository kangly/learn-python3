"""
Redis的先进先出队列
Redis 5.0 或以上
redis-py 3.2.1 或以上
"""

from redis import Redis
from library.fifo_queue import FifoQueue

client = Redis(decode_responses=True)

q = FifoQueue(client, 'buy-request')

print(q.enqueue('tom-buy-book'))
print(q.enqueue('jack-buy-cola'))
print(q.enqueue('rose-buy-coffee'))

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


