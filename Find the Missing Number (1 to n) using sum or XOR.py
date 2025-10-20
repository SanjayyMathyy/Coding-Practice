#Using Sum
def find_missing_sum(nums):
    n = len(nums) + 1 
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [1, 2, 4, 5]
print(find_missing_sum(nums))
