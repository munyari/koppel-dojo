def sum_of_fibs():
    fib_sum = 0
    while True:
        fib_sum += yield fib_sum

def get_fibs():
    a, b = 0, 1
    sum_gen = sum_of_fibs()

    sum_gen.send(None)
    while True:
        yield sum_gen.send(b)
        c = b
        b = a + b
        a = c
