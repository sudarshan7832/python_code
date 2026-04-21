list1 = [1, 4, 2, 11, 4545, 6, 10, 12, 2, 3, 7, 2, 13]
prev = list1[0]
list2 = []
for i in range(0, 2):
    for n in range(1,len(list1)):
        if prev <= list1[n]:
            prev = list1[n]
    list2.append(prev)
    list1.remove(prev)
    prev = list1[0]
print(list2[1])
l2 = [1, 4, 2, 11, 4545, 6, 10, 12, 2, 3, 7, 2, 13]
c = 0
for i in range(2):
    for num in l2:
        if num > c:
            c = num
    l2.remove(c)
    c = 0
print(num)
print("hi hellow python")