text = "9aa99bbbb54cddddff32gfa"  #o/p a2b4c1d4f2g1f1
digits = "0123456789"
prev = text[0]
count = 1
str1 = ""
for i in range(1, len(text)):
    if text[i] not in digits:
        if text[i] == prev:
            count += 1
        else:
            if prev in digits:
                prev = text[i]
            else:
                str1 = str1 + prev + str(count)
                prev = text[i]
                count = 1
str1 = str1 + text[i] + str(count)
print(str1)