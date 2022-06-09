s=input("enter the string")
a=input("enter the string u want to check")
b=sorted(s)
c=sorted(a)
if b==c :
    print("the strings are anagram")
else:
    print("the strings are not anagram")