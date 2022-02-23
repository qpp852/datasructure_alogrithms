# from linked_list import LinkedList
import queue


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str({
            'value': self.value,
            'next': self.next
        })

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        print(self.first)
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            holding_node = self.last
            self.last = new_node
            holding_node.next = self.last
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return
        
        if self.length == 1:
            self.last = None
    
        self.length -= 1
        removed_node = self.first
        self.first = self.first.next
        return removed_node


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue('Joy')
    queue.enqueue('Matt')
    queue.enqueue('Pavel')
    queue.enqueue('Samir')
    print(queue.dequeue())
    print(queue.dequeue())
    queue.peek()
    
    



        
    