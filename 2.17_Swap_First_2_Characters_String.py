"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
"""


string = "hello world"  

char_list = list(string)

# Swap characters at index 2 and index 6
char_list[2], char_list[6] = char_list[6], char_list[2]

# Convert list back to string
new_string = "".join(char_list)

# Output new string  
print(new_string)  
