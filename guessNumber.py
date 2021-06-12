print('Welcome to the number guessing game')
n = 7
guess = 5
while(True):
    print('Guess a number')
    inp1 = int(input())
    guess = guess-1
    if(guess>0):
        if(inp1<n):
            print("oops.. your number is less than the hidden number... try again")
            print("you have ", guess, "guess left")
            continue
        elif(inp1>n):
            print("oops.. your number is greater than the hidden number... try again")
            print("you have ", guess, "guess left")
            continue
        elif(inp1==n):
            print("Great.. you guess the correct number which was ", n)
            break
        else:
            print("please enter a valid input")
    else:
        print("no guess left")
        break



