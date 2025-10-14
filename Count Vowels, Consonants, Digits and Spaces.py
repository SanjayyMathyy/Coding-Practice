s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for text in s:
    if text.isdigit():
        digits += 1
    elif text.lower() in 'aeiou':
        vowels += 1
    elif text == ' ':
        spaces += 1
    elif text.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
