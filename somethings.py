import time
import sys

print(time.asctime())
print(sys.argv[1])

def square(x):
        return x * x

def sum_of_squares(point):
        return square(point[0]) + square(point[1])

def fxy(f, x, y):
        return f(x) + f(y)

def count_digits(number):
        return len(str(number))

cube = lambda x: x ** 3

istrcmp = lambda x, y : x.upper() == y.upper()

print("square: " + str(fxy(square, 2, 3)))
print("sum of squares: " + str(fxy(sum_of_squares, (2,3), (4,5))))
print("cube: " + str(fxy(cube, 5, 3)))
print('count_digits: ' + str(count_digits(1456748)))
print(istrcmp('python', 'Python'))
print(istrcmp('LaTeX', 'Latex'))
print(istrcmp('a', 'b'))

