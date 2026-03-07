import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

positions = {5, 200, 1000, 100000}

results = {}

for i in range(1, max(positions) + 1):
    current = next(fib)
    if i in positions:
        results[i] = current
        print(f"Найдено {i}-е число: {current}")
