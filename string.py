string1=input("enter the string1:")
string2=input("enter the string2:")
string1=list(string1)
string2=list(string2)
for char in string2:
    if char in string1:
        string1.remove(char)

if len(string1)==0:
 print("no")
else:
 print("yes")