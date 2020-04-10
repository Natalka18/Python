import random
from queue import Queue


min_children = 1
max_children = 5  # ile maksymalnie dzieci może mieć wierzchołek


class Node(object):
    def __init__(self, value, neighbours):
        self.value = value
        self.neighbours = neighbours

    def add_child(self, child):
        self.neighbours.append(child)

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.neighbours:
            return False
        return True


def random_tree(height):
    if height == 0:
        return None
    max_number_of_nodes = max_children**height - 1
    available_nodes = list(range(1, max_number_of_nodes + 1))
    return generate_tree(height, available_nodes)


def generate_tree(height, nodes):
    if height == 0:
        return None
    root_value = random.choice(nodes)
    nodes.remove(root_value)
    # jedno poddrzewo musi mieć wysokość height - 1, pozostałe
    # mogą (nie muszą) być krótsze
    number_of_children = random.randint(min_children, max_children)
    root = Node(root_value, [])
    # dodajemy do korzenie najwyższe poddrzewo
    high_subtree = generate_tree(height - 1, nodes)
    if high_subtree is not None:
        root.add_child(high_subtree)
    # pozostałe będą miały losowe wysokości
    for i in range(number_of_children):
        subtree_height = random.randint(0, height - 1)
        subtree = generate_tree(subtree_height, nodes)
        if subtree is not None:
            root.add_child(subtree)
    return root


def bfs(root):
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print("rodzic: ", str(node))
        yield str(node)
        for child in node.neighbours:
            queue.put(child)
            print(str(child))


def dfs(node):
    yield str(node)
    for child in node.neighbours:
        yield from dfs(child)


t = random_tree(3)
print(list(bfs(t)))
print(list(dfs(t)))
