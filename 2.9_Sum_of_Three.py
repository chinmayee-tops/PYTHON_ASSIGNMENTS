"""
Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.
"""
n1=int(input("Input Number 1 : "))
n2=int(input("Input Number 2 : "))
n3=int(input("Input Number 3 : "))
sum=0
if n1==n2 or n1==n3 or n2==n3:
    print("Any two numbers are equal...")
    print("Then Sum = ",sum)
else:
    sum=n1+n2+n3
    print("Final Sum of these entered numbers : ",sum)
