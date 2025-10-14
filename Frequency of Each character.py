s = input("Enter a string: ")
freq={}
for text in s:
    if text in freq:
        freq[text]+=1
    else:
        freq[text]=1
print(freq)