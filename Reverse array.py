# arr = list(map(int, input("Enter the values for the array: ").split()))
# def reverse_array(a):
#     a.reverse()
#     print(a)
# reverse_array(arr)

arr = list(map(int, input("Enter the values for the array: ").split()))
def reverse_array(a):
    left=0
    right=len(a)-1

    while left<right:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1

reverse_array(arr)
print("Reversed Array:",arr)
