import sys
import os


def to_lower(directory):
    for subdir, dirs, files in os.walk(directory):  # wchodzi do wszystkich katalogów, zwraca trójkę
        for filename in files:
            path_to_file = os.path.join(subdir, filename)
            os.rename(path_to_file, path_to_file.lower())


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        to_lower(path)
    except IndexError:
        print("Wywołanie programu:", "python zad3.py sciezka\\do\\katalogu", sep='\n')
