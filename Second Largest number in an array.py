arr = list(map(int, input("Enter numbers: ").split()))

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

if second == float('-inf'):
    print("No second largest number (all numbers may be same)")
else:
    print("Second largest number is:", second)
