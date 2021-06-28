enumerate = lambda a : [(i, a[i]) for i in range(len(a))]
zip = lambda x, y : [(x[i], y[i]) for i in range(len(x))]
filter = lambda a, y : [x for x in a if y(x)]
map = lambda a, y : [y(x) for x in a]

triplets = lambda n : [(x, y, z) for x in range(1, n) for y in range(1, n) for z in range(1, n) if f(x,y,z)]
parse_csv = lambda filename : [line.strip().split(',') for line in read_file(filename)]
parse = lambda filename, d, c : [line.strip().split(d) for line in r_f(filename, c)]
r_f = lambda filename, c : [line for line in read_file(filename) if filter_file(line, c)]
read_file = lambda filename : open(filename).readlines()
filter_file = lambda line, c : c not in line
array = lambda a, b : [[None for i in range(b)] for i in range(a)] 
f = lambda x, y, z : x + y == z and x <= y
even = lambda x: x % 2 == 0
square = lambda x : x * x

a = [1, 2, 3, 4]
b = [2, 3, 5, 7]

print("zip", zip(a,b))
print("map", map(b, square))
print("filter", filter(a , even))
print("triplets", triplets(5))
print("enumerate", enumerate(b))
print("array", array(4,3))
print("parse_csv", parse_csv('a.csv'))
print("parse", parse('a.txt', '!', "#")) 
