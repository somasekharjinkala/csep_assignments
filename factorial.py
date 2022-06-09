def function(n):
    if(n==0)|(n==1):
        return 1
    else:
        return n*function(n-1)

n=int(input("enter the number "))
f=function(n)
print(f)