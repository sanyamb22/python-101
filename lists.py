list1 = ["first", "second", "third", "fourth", "fifth", 44]
print(list1)
list2 = [2, 7, 9, 11, 3]
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
#list slicing just like string
print(list2[3])
#negative slicing
print(list2[::-1])
print(min(list2))
print(max(list2))
# adding element at the end of the list
list2.append(8)
print(list2)

# blank list and adding elements in it
list3 = []
list3.append(1)
list3.append(2)
list3.append(3)
print(list3)

# adding element at a particular index
list3.insert(1, 4)
print(list3)

# removing particular element
list3.remove(4)
print(list3)

# removing last element
list3.pop()
print(list3)

# tuple 
tuple1 = (3,4,5)    
print(tuple1)

# swapping two numbers 
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)
