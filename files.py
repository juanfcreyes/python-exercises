open_file_lines = lambda filename : open(filename).readlines()
reverse_line = lambda x: x[::-1]
search = lambda x, y : y in x

def charcount(filename):
    return len(open(filename).read())

def wordcount(filename):
    return len(open(filename).read().split())

def linecount(filename):
    return len(open_file_lines(filename))

def reverse_file(filename):
    return open_file_lines(filename)[::-1]

def reverse_file_lines(filename):
    lines = open_file_lines(filename)
    for i in range(len(lines)):
        lines[i] = reverse_line(lines[i]).strip()
    return lines

def head(filename):
    return open_file_lines(filename)[:2]

def tail(filename):
    lines = open_file_lines(filename)
    return lines[2:len(lines)]

def grep(filename, key):
    lines = open_file_lines(filename)
    grep_array = []
    for line in lines:
        if (search(line, key)):
            grep_array.append(line)
    return grep_array

def split_line(line, width):
    split_array = []
    num_parts = (len(line) // width) + (1 if len(line) % width != 0 else 0)
    for i in range(num_parts):
        split_array.append(line[(i)*width:(i+1)*width].strip())
    return split_array

def wrap (filename, width):
    lines = open_file_lines(filename)
    wrap_array = []
    for line in lines:
       wrap_array = wrap_array + split_line(line, width)
    return wrap_array

def wordwrap(filename, width):
    lines = reverse_file(filename)
    wrap_array = []
    for line in lines:
        temp_array = line.split()
        temp_line = ""
        for item in temp_array:
            if (len(temp_line) + len(item) < width):
                temp_line = temp_line + item + " "
            else:
                wrap_array.append(temp_line)
                temp_line = item + " "
        wrap_array.append(temp_line)
    return wrap_array


def center_align(filename):
    lines = reverse_file(filename)
    max_len = 0
    for line in lines:
        if max_len < len(line):
            max_len = len(line)
    for index in range(len(lines)):
       spa_num = (max_len - len(lines[index])) // 2
       for i in range(spa_num):
           lines[index] = " " + lines[index]
    return lines;

file = open('foo.txt').readlines()
print(charcount('foo.txt'))
print(wordcount('foo.txt'))
print(linecount('foo.txt'))

print("ORIGINAL TEXT")
print("".join(open_file_lines('foo.txt')))

print("REVERSE TEXT")
print("".join(reverse_file('foo.txt')))

print("HEAD")
print("".join(head('foo.txt')))

print("TAIL")
print("".join(tail('foo.txt')))

print("GREP")
print("".join(grep('foo.txt', "sure")))

print("WRAP")
print("\n".join(wrap('foo.txt', 30)))

print("\nWORD WRAP")
print("\n".join(wordwrap('foo.txt', 30)))

print("CENTER ALING")
print("".join(center_align('foo.txt')))

print("\nREVERSE LINES")
print("\n".join(reverse_file_lines('foo.txt')))


