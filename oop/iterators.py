class reverse_iter:
    def __init__(self, n):
        self.i = 0
        self.n = len(n)
        self.d = n[::-1]
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            d = self.d[i]
            self.i += 1
            return d
        else:
            raise StopIteration()


y = reverse_iter([1, 2, 3, 4, 5])
for i in y:
    print(i)


def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")
    
f = foo()
for i in f:
    print(i)

def integers():
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

print(take(5, squares()))

a = (x*x for x in range(10))
print(sum(a))

pyt = ((x, y, z) for z in integers() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)
print(take(10, pyt))
