file = open("data.txt","r")
l11=[]
for line in file:
    if len(line.split())>1:
        l11.append(line.split())
        print(line.split())
print(l11)