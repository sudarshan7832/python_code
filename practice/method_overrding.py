class A():
    def add(self,a,b):
        return a+b

class B(A):
    def add(self,a,b):
        pass

str1="aabbbccccddfghddhk"
prev = str1[0]
c=1
str2=""
for i in range(1, len(str1)-2):
    if prev == str1[i]:
        c = c+ 1
        prev = str1[i]
    else:
        str2 = str2+prev+str(c)
        c = 1
        prev = str1[i]
str2=str2+prev+str(c)
print(str2)




d1= {"a":100,"b":200,"c":300}
d2= {"a":100,"b":200,"d":400}
#d3= {"a":200,"b":400,"c":300,"d":400}


