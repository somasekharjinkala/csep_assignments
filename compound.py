def function2(I,t):
    if(t==1):
        return I
    else:
        return I*function2(I,t-1)

p=int(input("enter the princple"))
t=int(input("enter the time period"))
r=int(input("enter the rate"))
i=(p*(1+r/100))
f=function2(i,t)
print(f)