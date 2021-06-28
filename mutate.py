def mutate(word):
    BASE58 = 'abcdefghijklmnopqrstuvwxyz' 
    mutations = set([])
    word_array = [x for x in word]
    base8_array = [x for x in BASE58] + [""]
    for i in range(len(word)):
        word_array = [x for x in word]
        for b in base8_array:
            word_array[i] = b
            mutations.add("".join(word_array))

    for i in range(len(word) + 1):
        word_array = [x for x in word]
        for b in BASE58:
            mutations.add("".join(word_array[:i]) + b + "".join(word_array[i:]))

    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            a = word[i]
            b = word[i+1]
            for j in range(len(word)):
                word_array = [x for x in word]
                word_array[i] = word_array[j]
                word_array[j] = a
                mutations.add("".join(word_array))
            for j in range(len(word)) :
                word_array = [x for x in word]
                word_array[i+1] = word_array[j]
                word_array[j] = b
                mutations.add("".join(word_array))
    return mutations

print("mutate", len(mutate("hello")))
print("helo in", 'helo' in mutate("hello"))
print("cello in", 'cello' in mutate("hello"))
print("helol in", 'helol' in mutate("hello"))
