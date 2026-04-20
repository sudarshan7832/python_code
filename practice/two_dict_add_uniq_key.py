d1= {"a":100,"b":200,"c":300}
d2= {"a":100,"b":200,"d":400} #o/p {'a': 200, 'b': 400, 'c': 300, 'd': 400}
d3 = {}

keys1=list(d1.keys())
keys2=list(d2.keys())
keys3=list(keys1+keys2)
print(keys3)
unique = []
[unique.append(i) for i in keys3 if i not in unique]
print(unique)
for key in unique:
    if key in d1 and key in d2:
        d3[key]=d1[key] + d2[key]
    else:
        #d3[key] = d1[key] or d2[key]
        #d3[key] = d2[key]
        if key in d1:
            d3[key]=d1[key]
        else:
            d3[key]=d2[key]
print(d3)