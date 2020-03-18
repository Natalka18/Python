def all_subsets(s):
    if not s:
        return [[]]
    head = s[0]
    tail = s[1:]
    res = all_subsets(tail)
    return list(map(lambda t: [head] + t, res)) + res


lista = [1, 2, 3]
print(all_subsets(lista))
