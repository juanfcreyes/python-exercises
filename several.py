
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    return summation(n, lambda x: x)
   	
def sum_cubes(n):
    return summation(n, lambda x: x*x*x)


def pi_sum(n):
    return summation(n, lambda x: 8 / ((4*x-3) * (4*x-1)))
   

print(sum_naturals(100))
print(sum_cubes(100))
print(pi_sum(100))


def improve(update, close, guess=1):
   while not close(guess):
       guess = update(guess)
   return guess

def golden_update(guess):
   return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

phi = improve(golden_update, square_close_to_successor)
print(phi)


def average(x, y):
    return (x + y)/2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

result = sqrt(256)
print(round(result))

