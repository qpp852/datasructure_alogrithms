import json


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self) -> str:
        return str({'value': self.value, 'right': self.right, 'left': self.left})

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
            self.root = new_node
            return self

        current_node = self.root
        while True:
            if value >= current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return self
                current_node = current_node.right
            
            else:
                if current_node.left is None:
                    current_node.left = new_node
                    return self
                current_node = current_node.left
                    
    def lookup(self, value):
        if self.root is None:
            return None
        current_node = self.root
        while True:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                if current_node.right is None:
                    return None
                current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    return None
                current_node = current_node.left
    
    def remove(self, value):
        pass

                




if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(9)
    # tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree.lookup(9))
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.left.right.value)
    # print(tree.root.left.left.value)
    # print(tree.root.right.value)
    # print(tree.root.right.right.value)
    # print(tree.root.right.left.value)
    # print(tree.root.right.left.left.value)