def file_size(file_name):
    with open(file_name, 'r') as file:
        return sum([int(s[-1]) for s in [line.split() for line in file]])


print(file_size('test.txt'))
