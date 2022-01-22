class array:
    def __init__(self, length) -> None:
        self.length = length
        self.final_item_index = 0
        self.array = {i: None for i in range(self.length)}

    def print_array(self):
        print([i for i in self.array.values() if i ])
    
    # push(append)
    def push(self, value):
        self.array[self.final_item_index] = value
        self.final_item_index += 1
        return self.print_array()

    # pop(remove final value)
    def pop(self):
        self.array[self.final_item_index - 1] = None
        self.final_item_index -= 1
        return self.print_array()

    # unshift(prepend/insert)
    def unshift(self, index, value):
        if index > self.final_item_index:
            self.push(value)
            return

        temp = self.final_item_index
        
        while temp >= index:
            self.array[temp + 1] = self.array[temp]
            temp -= 1

        self.array[index] = value
        self.final_item_index += 1
        return self.print_array()

    # remove
    def remove(self, index):
        temp = index
        while temp < self.final_item_index - 1:
            self.array[temp] = self.array[temp + 1]
            temp += 1
        self.final_item_index -= 1
        self.array[self.final_item_index] = None
        return self.print_array()

if __name__ == "__main__":
    arr = array(100)
    arr.push('a')
    arr.push('b')
    arr.push('c')
    arr.push('d')
    arr.pop()
    arr.unshift(2, '123')
    arr.remove(1)
    print(arr.array)