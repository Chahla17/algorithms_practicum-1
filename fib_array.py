def fib(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    if n in {0}:
        return [n]

    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append(fib_array[i-2] + fib_array[i-1])

    return fib_array


if __name__ == '__main__':
    n = int(input('N Fibonacci number: > '))
    print(f'Result is: {fib(n)}')