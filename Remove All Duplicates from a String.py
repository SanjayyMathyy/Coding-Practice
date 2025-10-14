s = "programming"
emp = ""

for text in s:
    if text not in emp:
        emp += text

print(emp)