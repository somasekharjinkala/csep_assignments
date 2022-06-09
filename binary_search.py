def binary_search(key,arr,lb,ub):
    if(lb<=ub):
        mid=(lb+ub)//2
        if key==arr[mid]:
            print("key found at:-",mid)
            return
        elif key<arr[mid] :
            binary_search(key,arr,lb,mid-1)
        else:
            binary_search(key,arr,mid+1,ub)
    else:
        print("key not found")
    
n=int(input("enter the no. of elements"))
arr=[]
for i in range(0,n):
    l=int(input("Enter the number"))
    arr.append(l)

key=int(input("enter the key u want to search"))
f=binary_search(key,arr,0,n)