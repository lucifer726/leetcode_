class Node(object):
    def __init__(self, k, v, next=None, prev=None):
        self.key = k
        self.val = v
        self.next = next
        self.prev = prev


# 双端链表
class DoubleList(object):
    # 初始化双向链表的数据
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # 在链表头部添加节点 x，时间 O(1)
    def addFirst(self, x):
        x.next = self.head.next
        x.prev = self.head
        self.head.next.prev = x
        self.head.next = x
        self.size += 1

    # 删除链表中的x节点（x一定存在）
    # 由于是双链表且给的是目标Node节点，时间O(1)
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    # 删除链表中最后一个节点，并返回该节点，时间O(1)
    def removeLast(self):
        if self.size == 0:
            return None
        last_node = self.tail.prev
        self.remove(last_node)
        return last_node

    # 返回链表长度，时间 O(1)
    def getSize(self):
        return self.size


# LRU Cache
class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.map = dict()
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        val = self.map[key].val
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        new_item = Node(key, value)
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.addFirst(new_item)
            self.map[key] = new_item
        else:
            if self.cap == self.cache.getSize():
                last_node = self.cache.removeLast()
                self.map.pop(last_node.key)
            self.cache.addFirst(new_item)
            self.map[key] = new_item


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1))
    print(lRUCache.put(2, 2))
    print(lRUCache.get(1))
    print(lRUCache.put(3, 3))
    print(lRUCache.get(2))
    print(lRUCache.put(4, 4))
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
