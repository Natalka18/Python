import time


# drukuje czas wykonywania funkcji f w sekundach
def executing_time(f):
    def modified_f(*args, **kwargs):
        start = time.time()
        returned_value = f(*args, **kwargs)
        end = time.time()
        print("Czas w sekundach: ", end - start)
        return returned_value
    return modified_f


@executing_time
def f1(a, b, c):
    time.sleep(3)
    return a + b + c


print(f1(1, 2, 3))
