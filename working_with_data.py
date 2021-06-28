def reverse(array):
    return array[::-1]

def min(array):
    m = array[0]
    for i in array:
        if i < m:
            m = i
    return m

def cumulative_sum(array):
    acumulative_array = []
    for i in range(len(array)):
        acumulative_array.append(sum(array[:i+1]))
    return acumulative_array

def cumulative_product(array):
    acumulative_array = []
    for i in range(len(array)):
        acumulative_array.append(product(array[:i+1]))
    return acumulative_array

def unique(array):
    return list(set(array))

def dups(array):
    dups_array = []
    for x in unique(array):
        if (array.count(x) > 1):
            dups_array.append(x)
    return dups_array

def group(array, size):
    split_array = []
    index = 0
    num_parts = (len(array)//size) + (1 if (len(array) % size != 0) else 0)
    for i in range(num_parts):
        split_array.append(array[index:size*(i+1)])
        index = index + size
    return split_array
    
product = lambda x: x[0] if len(x) == 1 else x[0] * product(x[1: len(x)])
factorial = lambda x: x if (x == 1) else x * factorial(x - 1)

a = [1, 2, 3, 4, 5, 6]
b = [4, 5]
c = ["Hello", "World"]
x = range(10)
y = reverse(x)
print("range length: " + str(len(x)))
print("a: " + str(a))
print("b: " + str(b))
print("a + b: " + str(a + b))
print("b * 3: " + str(b * 3))
print("a[-3]: " + str(a[-3]))
print("a[-2]: " + str(a[-2]))
print("a[-1]: " + str(a[-1]))
print("product: " + str(product(a)))
print("factorial: " + str(factorial(4)))
print("min: " + str(min(c)))
print("cumulative sum: ", cumulative_sum(a))
print("cumulative product: ", cumulative_product(a))
print("unique:", unique(a + b))
print("dups:", dups(a + b + [1, 2]))
print("group:", group(a + b + [1, 2], 6))


