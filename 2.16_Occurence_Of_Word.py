"""
Write a Python program to count the occurrences of each word in a given sentence.
"""


string=input("Enter Any Sentance : ")
word=input("Enter a word : ")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Occurrences of ", word," : ",count)

