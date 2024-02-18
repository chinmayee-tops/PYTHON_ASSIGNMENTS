"""
Write python program that swap two number with temp variable and
without temp variable.
"""

num1=int(input("Input number 1 : "))
num2=int(input("Input number 2 : "))

print("\n Swapping two numbers with temp variable... ")
print("\n Before Swapping ... ")
print("Number 1 : ",num1)
print("Number 2 : ",num2)

temp=num1
num1=num2
num2=temp

print("\n After Swapping ... ")
print("Number 1 : ",num1)
print("Number 2 : ",num2)

print("\n Swapping two numbers without temp variable... ")
print("\n Before Swapping ... ")
print("Number 1 : ",num1)
print("Number 2 : ",num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("\n After Swapping ... ")
print("Number 1 : ",num1)
print("Number 2 : ",num2)

