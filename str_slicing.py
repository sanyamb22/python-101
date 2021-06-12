#few concepts about string slicing
str1 = "this is my first string"
# len funtion returns the number of characters in string
print(len(str1))
# [0:4] prints strings first 3 elements, 0 is included whereas 3 is not
print(str1[0:3])
# ::2 prints alternating characters
print(str1[::2])

#negative indexing"
print(str1[-4:-2])

#reversing the string
print(str1[::-1])

print(str1.count("t"))
print(str1.capitalize())
print(str1.lower())
print(str1.upper())
print(str1.replace("is", "are"))