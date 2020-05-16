from queue import Queue


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.queue = Queue(capacity)

    def enqueue(self, element: int) -> None:
        self.queue.put(element)

    def dequeue(self) -> int:
        return self.queue.get()

    def size(self) -> int:
        return self.queue.qsize()
