class stack:
    def __init__(self):
        self.array = []
    
    def peek(self):
        if self.array:
            return self.array[-1]
    
    def push(self, value):
        self.array.append(value)
        
    def pop(self):
        if self.array:
            v = self.array.pop()
            return v
        
        
class MyQueue(object):

    def __init__(self):
        self.main_stack = stack()
        self.sub_stack =stack()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.main_stack.push(x)
        # return self.main_stack.array

    def pop(self):
        """
        :rtype: int
        """
        if len(self.main_stack.array) == 0:
            return
        if len(self.main_stack.array) == 1:
            removed_val = self.main_stack.array.pop()
            return removed_val
        else:
            for i in range(len(self.main_stack.array)):
                val = self.main_stack.pop()
                self.sub_stack.push(val)
            
            removed_val = self.sub_stack.pop()
            
            for i in range(len(self.sub_stack.array)):
                val = self.sub_stack.pop()
                self.main_stack.push(val)
            return removed_val
            
    def peek(self):
        """
        :rtype: int
        """
        if self.main_stack.array:
            return self.main_stack.array[0]

    def empty(self):
        """
        :rtype: bool
        """
        if self.main_stack.array:
            return False
        return True

if __name__ == "__main__":
    queue = MyQueue()
    queue.push('Joy')
    queue.push('Matt')
    queue.push('Pavel')
    queue.push('Samir')
    print(queue.pop())
    print(queue.pop())
    print(queue.main_stack.array)