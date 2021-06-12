dict1 = {"A":"First", "B": "Second", "C": "third"}
print(dict1)

dict2 = {"a": "aaa", "b":"bbb", "c": "ccc", "d":{"f": "fff", "g":"ggg"}}
print(dict2)
print(dict2["a"])
print(dict2["d"]["g"])

# adding elements in dictionary
dict2["e"] = "eee"
print(dict2)
#or
dict2.update({"h":"hhh"})

# deleting element from dictionary
del dict2["e"]
print(dict2)

# using dictinary copy function
dict3 = dict2.copy() #it helps in keeping the data in dict2 safe if any manipulation happens to dict3
del dict3["d"]
print(dict3) #here we can see elements of dict2 in dict3 without "e"
print(dict2) #here we can see dict2 perfectly with all elements

#printing all the keys of dictionary
print(dict2.keys())
# prints key and key items in pairs
print(dict2.items())