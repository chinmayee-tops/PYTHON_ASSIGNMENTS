"""
Write a Python program to get the Factorial number of given number.

e.g Factorial number of 5 is 120.
5! = 5*4*3*2*1 = 120
3! = 3*2*1 =6

"""
num=int(input("Input a number to find out its Factorial : "))    
facto = 1    
if num < 0:
   print(" Factorial does not exist for negative numbers....")
   
elif num == 0:    
   print("The factorial of 0 is 1...")
   
else:    
   for i in range(1,num + 1):    
       facto = facto*i    
   print("The factorial of ",num," is ",facto)  
