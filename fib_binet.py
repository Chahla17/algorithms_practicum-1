def fib(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')
    
    a = (1 + 5 ** 0.5) / 2
    b = (1 - 5 ** 0.5) / 2
    return (a ** n - b ** n) / 5 ** 0.5


if __name__ == '__main__':
    n = int(input('N Fibonacci number: > '))
    print(f'Result is: {int(fib(n))}')