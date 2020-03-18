def flatten(t):
    for elem in t:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem


lista = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(lista)))
