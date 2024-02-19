"""
Write a Python function that takes a list of words and returns the length of the longest one.
"""

test_list = ['One', 'Two', 'Three', 'Four']
 
print("The original list : " + str(test_list))
 

res = max(test_list, key = len)
 

print("Maximum length string is : " + res)
