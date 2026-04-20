l = [2,1,5,2,6,3,9,8]
prev= l[0]
second_largest_num = []
c = 0
for i in range(2):
    for n in l[1:]:
        if prev <= n:
            prev = n
    second_largest_num.append(prev)
    l.remove(prev)
    prev = l[0]
print(second_largest_num[1])
print(l)
