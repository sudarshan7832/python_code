import re
"""
re nothing but regular expressions 
this module will have several methods like search, match sub, findall and etc.
Main the purpose re module is used to search the string/substring based on the given regular expression/pattern.
"""
"""
Using the re.search() method, we search for a value based on a given pattern.
It scans the string from left to right and returns the first match found
"""
str1="Sudhar24545m24m9s2a5n"
#pattern="[0-9][0-9][0-9][0-9][0-9]"
#pattern ="[0-9]+"
pattern='\d'
out=re.search(pattern,str1)
if out:
    print(out.group())
else:
    print("pattern not found")

out=re.findall(pattern,str1)
"""
What it does:
its Finds ALL matches
Returns a list of strings
"""
if out:
    print(out)
else:
    print("pattern not found")



