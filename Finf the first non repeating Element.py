def non_repeating(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return None

arr = [4, 5, 1, 2, 0, 4]
print(non_repeating(arr))  # Output: 5
