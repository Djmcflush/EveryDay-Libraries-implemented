class Node(object):
    val = int
    next = None
    prev = None
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

import gc
class Deque(object):
    head = None
    tail = None
    count = 0
    def __init__(self):
        node = None
        self.head = node
        self.tail = self.head
        self.count = 0
    def AppendLeft(self,val):
        if self.count == 0:
            self.head = Node(val)
            self.tail = self.head
        elif self.count ==1:
            node = Node(val)
            node.next = self.head
            self.head = node
        self.count +=1
        
        
    def AppendRight(self,val):
        if self.count == 0:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.count +=1
    def Size(self):
        return self.count
    def popLeft(self):
        if self.count ==0:
            return "Queue is empty"
        elif self.count ==1:
            val =self.head.val
            self.head = None
            self.tail = None
            self.count =0
            gc.collect()
            return val
        else:
            val = self.head.val
            self.head = self.head.next
            self.head.prev = None
            gc.collect()
            self.count -=1
            return val
    def popRight(self):
        if self.count ==0:
            return "Queue is empty"
        elif self.count ==1:
            val =self.head.val
            self.head = None
            self.tail = None
            self.count =0
            gc.collect()
            return val
        else:
            val =self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            gc.collect()
            self.count -=1
            return val
    def printQueue(self,switch=True):
        def g(switch,tmp):
            if switch:
                tmp = tmp.next
            else:
                tmp = tmp.prev
        c =[]
        if switch:
            tmp = self.head
        
        else:
            tmp = self.tail
        while tmp:
            c.append(tmp.val)
            tmp = g(switch,tmp)
        print(c)
        
if __name__ == __name__:
    queue = Deque()
    queue.AppendLeft(5)
    queue.AppendLeft(2)
    queue.printQueue()
    queue.printQueue(switch=True)
    print(queue.popLeft())