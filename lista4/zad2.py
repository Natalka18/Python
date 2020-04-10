import random
from queue import Queue


# zwraca listę reprezentującą drzewo binarne o wysokości height
# z niepowtarzającymi się numerami wierzchołków
def random_tree(height):
    if height == 0:
        return None
    max_number_of_nodes = 2**height - 1
    available_nodes = list(range(1, max_number_of_nodes + 1))
    return generate_tree(height, available_nodes)


def generate_tree(height, nodes):
    if height == 0:
        return None
    root = random.choice(nodes)
    nodes.remove(root)
    # prawe lub lewe poddrzewo ma wysokość height - 1, drugie ma wysokość
    # równą lub mniejszą height - 1
    # losujemy, które poddrzewo może być niższe
    short_subtree = random.choice([0, 1])
    # losujemy wysokość tego poddrzewa
    short_subtree_height = random.randint(0, height - 1)
    high_subtree_height = height - 1
    if short_subtree == 0:
        left_subtree = generate_tree(short_subtree_height, nodes)
        right_subtree = generate_tree(high_subtree_height, nodes)
    else:
        right_subtree = generate_tree(short_subtree_height, nodes)
        left_subtree = generate_tree(high_subtree_height, nodes)
    return [root, left_subtree, right_subtree]


# generator zwracający kolejne węzły drzewa w porządku bfs
# drzewo jest reprezentowane za pomocą listy opisanej w treści zadania
def bfs(tree):
    queue = Queue()
    queue.put(tree)
    while not queue.empty():
        node = queue.get()
        if isinstance(node, list):
            yield node[0]
            queue.put(node[1])
            queue.put(node[2])


t = random_tree(3)
print(t)
print(list(bfs(t)))
