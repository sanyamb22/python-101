# list1 = ["A", "B", "C", "D"]
# for item in list1:
#     print(item)
# list2 = [["A", "aaa"], ["B", "bbb"], ["C", "ccc"], ["D", "ddd"]]
# print(list2)
# for item in list2:
#     print(item)
# for item, item_elmt in list2:
#     print(item,"lower case 3 consecutive alphabet =", item_elmt)

list3 = ["a", 1, 2, "b", "c", 7, 8, "w"]
for item in list3:
    if str(item).isnumeric() and item>6:
        print(item)
    else:
        print("element is either not a number or less than 6")