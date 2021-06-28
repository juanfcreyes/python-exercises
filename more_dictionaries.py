def anagrams(array):
    wordsMap = {}
    for item in array:
        if "".join(sorted(item)) in wordsMap:
            wordsMap.get("".join(sorted(item))).append(item)
        else:
            wordsMap.setdefault("".join(sorted(item)),[item])
    return wordsMap

valuesort = lambda m: [pair[1] for pair in sorted(m.items(), key = lambda x : x[0])]
invertdict = lambda m: {pair[1]:pair[0] for pair in m.items()}
    
print("anagrams", anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
print("valuesort", valuesort({'x': 1, 'y': 2, 'a': 3}))
print("invertdict", invertdict({'x': 1, 'y': 2, 'z': 3}))
    
