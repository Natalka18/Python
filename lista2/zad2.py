import sys

def encode(file_name):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    try:
        with open(file_name, 'r') as file:
            bit_string = ""  # wczytany tekst z pliku jako ciąg bitów
            result = ""  # zakodowany ciąg
            for byte in file.read():
                bits = bin(ord(byte))[2:]  # [2:] odcina dwa pierwsze znaki z zapisu binarnego 0b1010000
                bits = "00000000"[len(bits):] + bits  # dopisuje z przodu zera, żeby było osiem znaków
                bit_string += bits
            while len(bit_string) >= 6:
                bits = bit_string[:6]
                bit_string = bit_string[6:]
                result += table[int(bits, base=2)]
            if bit_string:  # przypadek, gdy ilość bajtów nie była podzielna przez 3
                bit_string += "000000"[len(bit_string):]
                result += table[int(bit_string, base=2)]
            while len(result) % 4 != 0:
                result += '='
            return result
    except OSError:
        print("Błędne dane")


def decode(file_name):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    try:
        with open(file_name) as file:
            bit_string = ""  # odkodowany ciąg w postaci ciągu bitów
            result = ""  # odkodowany ciąg znaków
            for byte in file.read():
                if byte != '=':
                    bits = bin(table.index(byte))[2:]
                    bits = "000000"[len(bits):] + bits
                    bit_string += bits
            while len(bit_string) >= 8:
                bits = bit_string[:8]
                bit_string = bit_string[8:]
                result += chr(int(bits, base=2))
            return result
    except OSError:
        print("Błędne dane")


if __name__ == "__main__":
    try:
        if sys.argv[1] == "--encode":
            with open(sys.argv[3], 'w') as output_file:
                output_file.write(encode(sys.argv[2]))
        elif sys.argv[1] == "--decode":
            with open(sys.argv[3], 'w') as output_file:
                output_file.write(decode(sys.argv[2]))
        else:
            print("Sposób wywołania programu:\n python zad2.py --encode plik_wejściowy plik_wyjściowy\n",
                  "lub\n", "python zad2.py --decode plik_wejściowy plik_wyjściowy", sep='')
    except IndexError:
        print("Sposób wywołania programu:\n python zad2.py --encode plik_wejściowy plik_wyjściowy\n",
                  "lub\n", "python zad2.py --decode plik_wejściowy plik_wyjściowy", sep='')
