import timeit
def fib(n):
    if n == 0:
        return n

    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append(fib_array[i-2] + fib_array[i-1])

    return fib_array


n = int(input('N Fibonacci number: > '))
#print(f'Result is: {fib(n)}')
time = timeit.timeit(lambda: fib(n), number=1)
print(time)
