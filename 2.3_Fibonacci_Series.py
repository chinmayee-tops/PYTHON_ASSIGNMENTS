"""
Write a Python program to get the Fibonacci series of given range.

Fibonacci sequence, 1st two number is 1 and 0.
Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ... & so on up to range.
"""

num = int(input("Input a number :  "))
n1, n2 = 0, 1
c = 1

if num<=0:
    print("Please enter positive number to print Fibonacci Series ... ")

elif num==1:
    print("The Fibonacci Series up to ", num, " is : ", num)
    print(n1)

else:
    print(" The Fibonacci Series : ")
    while c<=num:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        c+=1

 
