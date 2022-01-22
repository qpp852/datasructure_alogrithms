 
class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None,
            'previous': None
        }

        self.tail = self.head
        self.length = 1

    def __repr__(self) -> str:
        
        return str({
            'head': self.head,
            'tail': self.tail
        })

    def append(self, value):
        new_node = {
            'value': value,
            'next': None,
            'previous': None
        }

        new_node['previous'] = self.tail
        self.tail['next'] = new_node
        self.tail = new_node

        self.length += 1

        return self.print_list()

    def prepend(self, value):
        new_node = {
            'value': value,   # new_node = {'value': 7, 'next': None, 'previous': None}
            'next': None, # 123 => {'value': 10, 'next': {'value': 5, 'next': {'value': 16, 'next': None}}}
            'previous': None
        }

        new_node['next'] = self.head
        self.head['previous'] = new_node
        self.head = new_node

        self.length += 1
        return self.print_list()

    def print_list(self):
        arr = list()
        current_node = self.head
        while current_node is not None:
            arr.append(current_node.get('value'))
            current_node = current_node.get('next')
        print(arr)

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
            
        new_node = {
            'value': value,
            'next': None,
            'previous': None
        }

        current_node = self.traverse_to_index(index)
        previous_node = self.traverse_to_index(index - 1)
        
        new_node['next'] = current_node
        current_node['previous'] = new_node

        previous_node['next'] = new_node
        new_node['previous'] = previous_node
        
        self.length += 1
        return self.print_list()

    def traverse_to_index(self, index):
        counter = index
        current_node = self.head
        
        while counter > 0:
            counter -= 1
            if current_node['next'] is not None:
                current_node = current_node['next'] 
            
        return current_node
        

    def remove(self, index):
        if index >= self.length:
            return self.print_list()
        
        if index == 0:
            self.head = self.head['next']
            self.head['previous'] = None
            self.length -= 1
            return self.print_list()

        leader = self.traverse_to_index(index-1)
        unwanted_node = leader['next']

        leader['next'] = unwanted_node['next']
        unwanted_node['next']['previous'] = leader
        
        self.length -= 1

        return self.print_list()


    
my_linked_list = DoublyLinkedList(10)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.prepend(1)
my_linked_list.prepend(12)
my_linked_list.insert(3, 66)
# my_linked_list.append(16)
# my_linked_list.prepend(1)
# my_linked_list.insert(2, 99)
# my_linked_list.insert(2, 88)
print(my_linked_list)
# print(my_linked_list.head['next']['previous'])
my_linked_list.remove(3)
# print(my_linked_list.print_list())
my_linked_list.remove(2)