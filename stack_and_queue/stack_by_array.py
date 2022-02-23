class Stack:
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        if self.array:
            return self.array[-1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        self.array.pop()

if __name__ == "__main__":
    stack = Stack()
    stack.push('google')
    stack.push('Udemy')
    stack.push('Discord')
    stack.pop()
    # stack.pop()
    # stack.pop()
    print(stack.array)
    # print(stack.length)




        
    