def transpose(matrix):
    """
        funkcja transponuje macierz matrix
        :param matrix: macierz zapisana w postaci ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
        :return: macierz transponowana dla matrix w tej samej postaci
    """
    matrix = [s.split() for s in matrix]
    return [' '.join(t) for t in [[row[index] for row in matrix] for index in range(len(matrix))]]


#  to samo co transpose(), ale z pętlami
def transpose_with_loops(matrix):
    t_matrix = []
    matrix = [s.split() for s in matrix]
    print(matrix)
    for index in range(len(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[index])
        t_matrix.append(new_row)
    print(t_matrix)
    t_matrix = [' '.join(t) for t in t_matrix]

    return t_matrix


print(transpose(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))
