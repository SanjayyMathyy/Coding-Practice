def factorial(f):
    if f==0 or f==1:
        return 1
    else:
        return f*factorial(f-1)
num=int(input("Enter the factorial number: "))
print(f"Factorial: {factorial(num)}")