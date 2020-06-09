import random


class Node:
    def __init__(self):
        self.goes_to = []
        self.flag = -1  # for the purpose of discover method


class Graph:
    def __init__(self, *args):
        self.map = {node: node.goes_to for node in args}
        self.all_nodes = [node for node in args]
        self.cycle = False
        # self.n_possible_spanning_trees = no_of_edges--C--(no_of_nodes_-_1)  -  no_of_cycles
        # a weighted graph is a graph with edges having weights

    def contains_cycle(self):
        while any([i.flag == -1 for i in self.all_nodes]) and self.cycle is False:
            node = random.choice(self.all_nodes)
            self.discover(node)
        return self.cycle

    def discover(self, node):
        if all([i.flag == 1 for i in self.all_nodes]):
            # if all the values are 0 or 1 then return false as all the element are visited
            self.cycle = False
            return

        if node.flag == 0:  # in the visiting list
            self.cycle = True
            return

        if node.flag == 1:  # already being visited
            return

        elif node.flag == -1:  # not visited yet
            node.flag = 0
            for i in node.goes_to:
                self.discover(i)
                i.flag = 1
            node.flag = 1


n1, n2, n3, n4, n5, n6 = Node(), Node(), Node(), Node(), Node(), Node()
n1.goes_to = [n2, n3]
n2.goes_to = [n3]
n3.goes_to = []
n4.goes_to = [n1, n5]
n5.goes_to = [n6]
n6.goes_to = [n4]
g1 = Graph(n1, n2, n3, n4, n5, n6)

print("hello")
print(g1.contains_cycle())



