def lensort(array):
    array.sort(key = lambda x: len(x))
    return array

def unique(array, key = None):
    if key == None:
        return list(set(array))
    else:
        unique_array = [] 
        for i in array:
            if key(i) not in unique_array:
                unique_array.append(i)
        return unique_array

def extsort(array):
    array.sort(key = lambda x: x.split('.')[1])
    return array


print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
print(unique(["python", "java", "Python", "Java"], key = lambda s: s.lower()))
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
