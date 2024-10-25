def return_evens(lst):
    for l in lst:
        if l % 2 == 0:
            yield l

eggs = [x for x in range(20)]

print(list(return_evens(eggs)))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

def fibonacci2():
    a, b = 0, 1
    while True:
        return a
        a, b = b, a + b