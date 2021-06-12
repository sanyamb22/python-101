var1 = 1
var2 = 10
print("enter an interger")
var3 = int(input())
if (var3 == var1):
    print(var3 , "is equal to ", var1)
elif (var3 == var2):
    print(var3 , "is equal to ", var2)
elif (var3 > var1 and var3 < var2):
    print(var3 ,"is greater than", var1 ,"but less than", var2)
elif (var3 > var2):
    print(var3 ,"is greater than ", var2)
else:
    print(var3 ,"is negative integer")

#using in keyword and working with a list
list1 = [1, 2, 3, 4]
print(list1)
if var3 in list1:
    print(var3,"is present in the list")
else:
    print(var3,"is not present in the list")
    