name = "madam"
empty_string = ""
for letter in name:
    empty_string = letter + empty_string
if empty_string == name:
    print("name is polindrome")
else:
    print("name is not polindrome")