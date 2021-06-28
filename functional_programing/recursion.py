import re

def product(n, m):
    if m == 1:
        return n
    else:
        r = product(n, m + 1) - n if m <= 0 else product(n, m - 1) + n
        return r

def flatten_list(a, result = None):
    if result is None:
        result = []
    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)
    return result

def unflaten_prototype_1(m):
    res = dict()
    for k, v in m.items():
        l = k.split('.')[::-1]
        value = v
        for i in l:
            value = {i : value}
        if l[len(l)-1] in res:
            res[l[len(l)-1]].update(value[l[len(l)-1]])
        else:
            res.update(value)
    return res

def get_unflatten_element(key, value):
    k = next(key)
    try:
        return get_unflatten_element(key, {k: value } )
    except StopIteration:
        return {k : value}

def unflatten_dict(m, result = None):
    if result is None:
        result = dict()
    for k, v in m.items():
        it = iter(k.split('.')[::-1])
        value = get_unflatten_element(it, v)
        if k[0] in result:
            result[k[0]].update(unflatten_dict(value[k[0]], result[k[0]]))
        else:
            result.update(value)
    return result

def flatten_dict(d, p = "", result = None):
    if result is None:
        result = dict()
    for k, v in d.items():
        s = p + str(k)
        if isinstance(v, dict):
            flatten_dict(v, s + ".", result)
        else:
            result.setdefault(s, v)
    return result

def treemap(f, l, result = None):
    if result is None:
        result = []
    for i in l:
        if isinstance(i, list):
            result.append(treemap(f, i, []))
        else:
            result.append(f(i))
    return result

def tree_reverse(l, result = None):
    if result is None:
        result = []
    for i in l:
        if isinstance(i, list):
            result.append(tree_reverse(i,[]))
        else:
            result.append(i)
    return result[::-1]


print("unflatten_dict: ", unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
print("product: ", product(-7, 5))
print("flatten_list: ", flatten_list([ [1, 2, [3, 4, [8 , 9]] ], [5, 6], 7]))
print("flatten_dict: ", flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
print("flatten_dict2: ", flatten_dict({'a': { 4 : 1}, 'b': {'x': 2, 'y': {'w' : 5}}, 'c': 4}))
print("unflatten_prototype", unflatten_dict({'a.4': 1, 'b.x': 2, 'b.y.w': 5, 'c': 4}))
print("unflatten_prototype", unflatten_dict({'a.w' : 1}))
print("unflatten_prototype", unflatten_dict({'a.w.y' : 1, 'a.w.1': 2}))
print("unflatten_prototype: ", unflatten_dict({'a.w.y' : 1, 'a.z.1': 2}))
print("flatten_dict: ", flatten_dict({'a': {'w': {'y': 1, '1': 2}}}))
print("unflatten_prototype: ", unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
print("treemap: ", treemap(lambda x: x*x, [1, 2, [3, 4, [5 ,[6]]]]))
print("tree_reverse: ", tree_reverse([[1, 2], [3, [4, 5]], 6, [7, [8, 9, [10]]]]))

