# working with sets in python
set1 = set([1,2,3,4])
print(type(set1))
print(set1)

# we can also create set with different method
# we can first create a list and then assign it to a set

list1 = ["a", "b", "c", "d"]
print(type(list1))
set2 = set(list1)
print(type(set2))
print(set2)

#adding element in a set
set1.add(5)
print(set1)
# but the value inside a set must be unique, if i add 5 again in set1 it will not add
set1.add(5)
print(set1)  #no addition took place, print stat. showed that

#union of set
S1 = set1.union({1, 2, 3, 4, 5, 6})
print(set1, S1)

#intersection of set
S2 = set1.intersection({1, 2, 3})
print(set1, S2)

# remving element from set
set1.remove(3)
print(set1)