"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing'
then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
"""



MyString1="relaying"
l=len(MyString1)

print(l)

if "ing" in MyString1:
        if l>3:
            print("Yes! 'ing'  is present in the string.")
            MyString2=MyString1.replace("ing","ly")
            print(MyString2)
        else:
            print("No! 'ing' is not present.")
else:
    print("String will be remained unchanged... ",MyString1)
