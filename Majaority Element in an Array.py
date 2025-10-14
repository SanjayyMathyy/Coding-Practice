def majority_element(arr):
    major=None
    count=0
    for num in arr:
        if count==0:
            major=num
            count=1
        elif num==major:
            count+=1
        else:
            count-=1
    count=0
    for num in arr:
        if num == major:
            count+=1
    if count>len(arr)//2:
        return major
    else:
        return None

arr=[3,3,3,2,1,3,2,2,2,3,3]
print("Majority element: ",majority_element(arr))