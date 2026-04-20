file = open('data.txt','r')
d = {}

columns=[]
d={}

for line in file:
    if len(line.split())>1:
        if not columns:
            columns = line.split()
        elif not d:

            d[columns[0]] = [line.split()[0]]
            d[columns[1]] = [line.split()[1]]
            d[columns[2]] = [line.split()[2]]
            d[columns[3]] = [line.split()[3]]
            d[columns[4]] = [line.split()[4]]
            d[columns[5]] = [line.split()[5]]
        elif d:

            d[columns[0]] = d[columns[0]] + [line.split()[0]]
            d[columns[1]] = d[columns[1]] + [line.split()[1]]
            d[columns[2]] = d[columns[2]] + [line.split()[2]]
            d[columns[3]] = d[columns[3]] + [line.split()[3]]
            d[columns[4]] = d[columns[4]] + [line.split()[4]]
            d[columns[5]] = d[columns[5]] + [line.split()[5]]
print(d)

# d={}
#
# l1=[[1,20,30,40,50],[2,100,200,300,400],[3,400,500,600,700]]
# l2 = []
# l3=[]
# #o/p:d={"S_NO":[1,2,3]}
# for i in range(0, len(l1)):
#     l2.append(l1[i][0])
#     l3.append(l1[i][1])
# d["S.NO"] = l2
# d["role"]=l3
# print(d)


