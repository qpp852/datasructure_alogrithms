
class Graph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_node(self, node):
        if node in self.adjacent_list.keys():
            return
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)

    def show_connections(self):
        pass