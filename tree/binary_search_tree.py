from threading import currentThread


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def next(self, node, value):
        if value > node.value:
            if node.right:
                return node.right
        elif value < node.value:
            if node.left:
                return node.left
        return None
                


    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = Node(value)
        
        if value > self.root.value:
            self.root.right
        
        current = self.root
        next = self.next(current, value)
        while next is not None:
            current = next
            next = self.next(current, value)
        
        if value > current.value:
            current.right = new_node
        elif value < current.value:
            current.left = new_node
        else:
            return 

    def lookup(self, value):
        pass



if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree.root.value)
    print(tree.root.left.value)
    print(tree.root.left.right.value)
    print(tree.root.left.left.value)
    print(tree.root.right.value)
    print(tree.root.right.right.value)
    print(tree.root.right.left.value)