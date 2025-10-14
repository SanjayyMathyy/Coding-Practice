arr = list(map(int, input("Enter numbers: ").split()))

i = 0

for j in range(len(arr)):
    if arr[j] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

print("Array after moving zeros to the end:", arr)