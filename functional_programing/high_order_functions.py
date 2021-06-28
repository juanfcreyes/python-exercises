import time

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g

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

def profile(f):
    def g(x):
        start_time = time.time()
        value = f(x)
        end_time = time.time()
        print('execution time', end_time - start_time)
        return value   
    return g

def vectorize(f):
    def g(x):
        return [ f(i) for i in x]
    return g

def unixcommand(f):
    def g(filenames):
        printlines(out for line in readlines(filenames)
                           for out in f(line))
    return g

@unixcommand
def cat(line):
    yield line

@unixcommand
def lowercase(line):
    yield line.lower()

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def square(x): return x * x

def lenght(x): return len(x)



g = profile(fib)
print(g(20))
f = vectorize(square)
print(f([1, 2, 3]))

g = vectorize(len)
print(g(["hello", "world"]))
print(g([[1, 2], [2, 3, 4]]))



