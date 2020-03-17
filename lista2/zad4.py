import sys
import os
import hashlib


def repchecker(directory):
    """
    :param directory: sciezka do pliku
    :return: slownik z parami postaci ((rozmiar pliku, wartość funkcji hashującej), zbiór nazw plików)
    """
    # słownik par:
    # ((rozmiar pliku, wartość funkcji hashującej), zbiór nazw plików o danym rozmiarze i wartości funkcji hashującej)
    files_dict = {}
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            path_to_file = os.path.join(subdir, filename)
            with open(path_to_file, 'r') as f:
                file_size = os.path.getsize(path_to_file)
                content = f.read()
                hash_ = hashlib.md5(content.encode()).hexdigest()
                if (file_size, hash_) in files_dict:
                    files_dict[(file_size, hash_)].add(path_to_file)
                else:
                    files_dict[(file_size, hash_)] = set()
                    files_dict[(file_size, hash_)].add(path_to_file)
    return files_dict


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        dictionary = repchecker(path)
        for key in dictionary.keys():
            for file in dictionary[key]:
                print(file)
            print('---------------------------------')
    except IndexError:
        print("Wywołanie programu:", "python zad4.py sciezka\\do\\katalogu", sep='\n')
