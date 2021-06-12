# i = 0
# while(True):                #True will make it infinite loop 
#     if(i<5):
#         i = i+1
#         continue
#     print(i+1, end=" ")
#     if(i==40):
#         break
#     i=i+1

print("Welcome")
while(True):
    print("Enter a number that is above 100")
    inp1 = int(input())
    if(inp1<100):
        print("your entered number is less than 100... try again")
        continue

    else:
        print("Great... your entered number is ", inp1, "which is greater than 100")
        break

