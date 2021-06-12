import random
options = ["r","p","s"]
user_score = 0
cpu_score = 0
turns = 0

print("Welcome to the Rock, Paper, Scissors Game!!!")
# inp1 = input("Press 'Y' to play the game, 'N' to exit the game")

while(True):
    cpuOpt = random.choice(options)
    userOpt = input("Make your Choice!\n r. for Rock\t p. for Paper\t s. for Scissors\t Press any other key to quit\n")
    if userOpt == "r":
        if cpuOpt == userOpt:
            print("Its a tie!")
            turns = turns + 1
            continue
        elif cpuOpt == "p":
            print("You Loose")
            cpu_score+=1
            turns = turns + 1
            continue
        else:
            print("you win!")
            user_score+=1
            turns = turns + 1
            continue
    elif userOpt == "p":
        if cpuOpt == userOpt:
            print("Its a tie!")
            turns = turns + 1
            continue
        elif cpuOpt == "s":
            print("You Loose")
            cpu_score+=1
            turns = turns + 1
            continue
        else:
            print("you win!")
            user_score+=1
            turns = turns + 1
            continue
    elif userOpt == "s":
        if cpuOpt == userOpt:
            print("Its a tie!")
            turns = turns + 1
            continue
        elif cpuOpt == "r":
            print("You Loose")
            cpu_score+=1
            turns = turns + 1
            continue
        else:
            print("you win!")
            user_score+=1
            turns = turns + 1
            continue
    else:
        print("Thanks for Playing the game!!!")
        break

if cpu_score > user_score:
    print("You lost the game")
    output = f"cpu score was {cpu_score} whereas your score was {user_score} in {turns} turns"
    print(output)
elif cpu_score < user_score:
    print("You won the game")
    output = f"cpu score was {cpu_score} whereas your score was {user_score} in {turns} turns"
    print(output)
else:
    print("the game was tied")
    output = f"cpu score was {cpu_score} whereas your score was {user_score} in {turns} turns"
    print(output)



