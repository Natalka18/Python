from numpy.random import randint


def qsort(xs):
    if not xs:
        return []
    pivot = xs[0]
    xs = xs[1:]
    elements_lt = list(filter(lambda x: x < pivot, xs))
    elements_gt = list(filter(lambda x: x >= pivot, xs))
    return qsort(elements_lt) + [pivot] + qsort(elements_gt)


lista = list(randint(1, 21, 20))
print("Lista:", lista)
print("Lista posortowana", qsort(lista))
