def fib(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


if __name__ == '__main__':
    n = int(input('N Fibonacci number: > '))
    print(f'Result is: {fib(n)}')