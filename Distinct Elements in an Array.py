arr = [1, 2, 2, 3, 4, 3, 5]
distinct_elements = []

for num in arr:
    if num not in distinct_elements:
        distinct_elements.append(num)

print(len(distinct_elements))
