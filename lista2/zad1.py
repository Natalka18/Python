import os
import sys


def get_file_size(file_path):
    """
        path - ścieżka do pliku.
        Funkcja zwraca krotkę (num_bytes, num_words, num_lines, max_line_length), gdzie:
            num_bytes - ilość bajtów pliku path,
            num_words - ilość słów w pliku path,
            num_lines - ilość słów w pliku path,
            max_line_length - maksymalna długość linii w pliku path
    """
    try:
        num_bytes = os.path.getsize(file_path)
        with open(file_path, 'r') as file:
            num_lines = 0
            num_words = 0
            max_line_length = 0
            for line in file:
                num_lines += 1
                num_words += len(line.split())  # każdy biały znak jest separatorem (wiele spacji pod rząd to separator)
                if len(line) > max_line_length:
                    max_line_length = len(line)
            return num_bytes, num_words, num_lines, max_line_length
    except OSError:
        print("Błędne dane")


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        size = get_file_size(path)
        print("liczba bajtów:", size[0])
        print("liczba słów:", size[1])
        print("liczba linii:", size[2])
        print("maksymalna długość linii:", size[3])
    except IndexError:
        print("Podaj nazwę pliku")
