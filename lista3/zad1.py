def transpose(matrix):
    """
        funkcja transponuje macierz matrix
        :param matrix: macierz zapisana w postaci ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
        :return: macierz transponowana dla matrix w tej samej postaci
    """
    matrix = [s.split() for s in matrix]
    return [' '.join(t) for t in [[row[index] for row in matrix] for index in range(len(matrix))]]


print(transpose(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))
