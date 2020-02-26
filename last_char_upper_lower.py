#code to convert last character of each word in the string to uppercase and lowercase.
line="i love python programming ! Do you like it ?"
a=line.split()
b=""
for i in a:
    b+=" "+i[:len(i)-1]+i[-1].upper()
print(b)
line="PYTHON PROGRAMMING"
a=line.split()
b=""
for i in a:
     b+=" "+i[:len(i)-1]+i[-1].lower()
print(b)
