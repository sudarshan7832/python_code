text = "9aabb675baccccdaa"
digit = "0123456789"
count_char = ""
c=0
for char in text:
    if char not in digit:
        if char not in count_char:
            for char2 in text:
                if char == char2:
                    c = c + 1
            count_char = count_char + char + str(c)
            c = 0
print(count_char)
print("checking git hub")
