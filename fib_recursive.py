def fib(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    if n == 0:
        return 0
    if n in {1, 2}:
        return 1
    else:
        return(fib(n-1) + fib(n-2))


if __name__ == '__main__':
    n = int(input('N Fibonacci number: > '))
    print(f'Result is: {fib(n)}')