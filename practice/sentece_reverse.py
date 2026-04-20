text = "my name is sudarshan"
reverse =  ""
for char in text.split():
    reverse = reverse + char[::-1] + " "
print(reverse)