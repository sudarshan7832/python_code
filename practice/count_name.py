file = open("demo.txt", 'r')
# read=file.readlines()
required_name = "sudarshan"
# #print(read)
# #print(len(read))
# count = 0
# for line in read:
#     line2=line.split()
#     c=line2.count(required_name)
#     count =count+c
# print(count)
print(file)
import re
count=0
for line in file:
    print(line)
    line = line.strip()
    re_findall=re.findall(required_name,line)
    #print(re_findall)
    length = len(re_findall)
    count+=length
    # split_line=line.split()
    # if required_name in split_line:
    #     c=split_line.count(required_name)
    #     count =count+1
print(count)
