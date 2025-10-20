def subarray_with_given_sum(arr, target):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target and start < end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return arr[start:end + 1]
    return None
arr = [1, 2, 3, 7, 5]
target = 12
print(subarray_with_given_sum(arr, target))
