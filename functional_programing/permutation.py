def trace(f):
    f.indent = 0
    def g(x):
        print('|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        value = f(x)
        print('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
@trace
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def count_change(value, coins):
    s = 0
    if value < 0:
        return 0
    if value == 0:
        return 1
    for i in range(len(coins)):
        s += count_change(value - coins[i], coins[i:])
    return s
    
def permute(a):
    l = len(a)
    if l == 0:
        return []
    if l == 1:
        return [a]
    result = []
    for i in range(l):
        e = a[i]
        suba = a[:i] + a[i+1:]
        for p in permute(suba):
            result.append([e] + p)
    return result

print(count_change(4 , [1, 2]))
print(count_change(10, [1, 5]))
print(count_change(10, [2, 5]))
print(count_change(10, [1, 3]))
print(count_change(10, [1, 2]))
print(count_change(10, [1, 2, 5]))
print(count_change(5, [1, 2, 3]))
print(count_change(100, [1, 5, 10, 25, 50]))
print(permute([1, 2, 3]))
print(fib(5))
print(fib(3))



