"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""
MyString1="Python is not poor language."

if "not poor" in MyString1:
        print("Yes! it is present in the string.")
        MyString2=MyString1.replace("not poor","good")
        print(MyString2)
else:
        print("No! it is not present.")

