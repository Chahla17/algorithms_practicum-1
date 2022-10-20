def fib_eo(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')
    
    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, int(repr(previous + fib_number)[-1])

    return 'even' if fib_number % 2 == 0 else 'odd'


if __name__ == '__main__':
    n = int(input('N Fibonacci number: > '))
    print(f'Result is: {fib_eo(n)}')