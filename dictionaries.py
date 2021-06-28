def count_frequency(array):
    frequency = {}
    for w in array:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
    return open(filename).read().split()

def count_words(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in sorted(frequency.items(), key = lambda x: -x[1]):
        print(word, count)

def count_characters(filename):
    file = "".join(open(filename).read().strip().split())
    for char, count in sorted(count_frequency(file).items(), key = lambda x: -x[1]):
        print(char, count)

def main(filename):
    count_characters(filename)
    
if __name__ == "__main__":
    main("foo.txt")
