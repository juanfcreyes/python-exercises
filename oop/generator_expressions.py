import os

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def cat(lines):
    for line in lines:
        print(line, end="")

def filer(num, lines):
    for line in lines:
        return (line for line in lines if len(line) > num)

def main(pattern, filenames):
    print("cat")
    cat(readfiles(filenames))
    print("grep")
    cat(grep(pattern, readfiles(filenames)))


    
main("pass", os.listdir(os.getcwd()))

print("filer")
cat(filer(40, readfiles(os.listdir(os.getcwd()))))
