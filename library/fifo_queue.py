class FifoQueue:
    """ 实现先进先出队列 """

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def enqueue(self, item):
        """ 将给定的元素写入队列，并返回当前队列的元素数量 """
        return self.client.rpush(self.key, item)

    def dequeue(self):
        """ 移除并返回当前队列中入队时间最长的元素 """
        return self.client.lpop(self.key)
