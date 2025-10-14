arr=list(map(int,input("Enter the values for the array: ").split()))
def sort(A):
    n=len(A)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if A[i-1]<A[i]:
                flag=True
                A[i-1],A[i]=A[i],A[i-1]
sort(arr)
print(arr)
m=len(arr)
print(m)
print(f"The Maximum Element in the array is: {arr[0]} and the minimum value is: {arr[m-1]}")

