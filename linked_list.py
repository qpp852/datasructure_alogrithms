 
class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }

        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            'value': value,
            'next': None
        }

        self.tail['next'] = new_node
        self.tail = new_node

        self.length += 1

        return self.head  

    def prepend(self, value):
        new_node = {
            'value': value,
            'next': self.head # 123 => {'value': 10, 'next': {'value': 5, 'next': {'value': 16, 'next': None}}}
        }

        self.head = new_node

        self.length += 1
        return self.head

    def print_list(self):
        arr = list()
        current_node = self.head
        while current_node is not None:
            arr.append(current_node.get('value'))
            current_node = current_node.get('next')
        return arr

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
            
        if index == 0:
            return self.prepend(value)
            
        new_node = {
            'value': value,
            'next': None
        }

        current_node = self.head
        current = index
        while current > 0:
            previous_node = current_node
            current_node = current_node['next']
            current -= 1

        new_node['next'] = current_node
        previous_node['next'] = new_node
        
        self.length += 1
        return self.head

    def __repr__(self) -> str:
        
        return str({
            'head': self.head,
            'tail': self.tail
        })

my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
my_linked_list.insert(20, 88)
print(my_linked_list.print_list())
