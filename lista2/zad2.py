def encode(file_name):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    try:
        with open(file_name, 'r') as file:
            bit_string = ""
            result = ""
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
            
    except OSError:
        print("Błędne dane")
