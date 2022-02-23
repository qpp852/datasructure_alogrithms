# from linked_list import LinkedList
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str({
            'value': self.value,
            'next': self.next
        })

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
        self.length += 1

    def pop(self):
        if self.length == 0:
            return

        if self.length == 1:
            self.bottom = None
            
        self.top = self.top.next
        self.length -= 1

if __name__ == "__main__":
    stack = Stack()
    stack.push('google')
    stack.push('Udemy')
    stack.push('Discord')
    # stack.pop()
    # stack.pop()
    # stack.pop()
    print(stack.peek())
    print(stack.length)




        
    