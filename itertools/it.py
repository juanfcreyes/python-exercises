import itertools

def peep(it):
    l = list(it)
    return (l[0], iter(l))

def enumerate(it):
    index = 0
    for i in it:
        yield (index, i)
        index += 1

def infinite():
    index = 0
    while True:
        index += 1
        yield index

def value(it):
    try:
        value = next(it)
    except StopIteration:
        value = None
    return value


def izip(it1, it2):
    iter1 = iter(it1)
    iter2 = iter(it2)
    while True:
        value1 = value(iter1)
        value2 = value(iter2)
        if value1 == None and value2 == None:
            break
        else: 
            yield (value1, value2)

    
it1 = iter([1, 2, 3])
it2 = iter([4, 5, 6])
itertools.chain(it1, it2)

for i in itertools.chain(it1, it2):
    print(i)

for x, y in itertools.zip_longest(["a", "b", "c"], [1, 2, 3, 4]):
    print(x, y)

for x, y in izip(["a", "b", "c"], [1, 2, 3, 4]):
   print(x, y)

x, it1 = peep(iter(range(5)))
print(x, list(it1))
print(list(enumerate(["a", "b", "c"])))
for i, c in enumerate(["a", "b", "c"]):
    print(i, c)

