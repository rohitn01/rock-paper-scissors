import random



print("Let's play rock, paper, scissors!\n")

cont = 9
win = 0
draw = 0
loss = 0
while(cont == 9):
    print("Press 1 for rock, 2 for paper, and 3 for scissors.\n")
    a = int(input())
    b = random.randint(1, 4)

    if(a == 1 or a == 2 or a == 3):
        if(a == b):
            print("Draw! Try again!\n")
            draw += 1
            cont = 9
            
        else:
            if(a == 1 and b == 2):
                print("*Throws Paper* Paper beats Rock. You lose!\n")
                loss += 1
            if(a == 2 and b == 1):
                print("*Throws Rock* Paper beats Rock. You win!\n")
                win += 1
            if(a == 2 and b == 3):
                print("*Throws Scissors* Scissors beats Paper. You lose!\n")
                loss += 1
            if(a == 3 and b == 2):
                print("*Throws Paper* Scissors beats Paper. You win!\n")
                win += 1
            if(a == 3 and b == 1):
                print("*Throws Rock* Rock beats Scissors. You lose!\n")
                loss += 1
            if(a == 1 and b == 3):
                print("*Throws Scissors* Rock beats Scissors. You Win!\n")
                win +=1

            print("Try Again? (9 = yes, 0 = no)")
            cont = int(input())
            
    else:
        print("Incorrect input, try again!\n")
        cont = 9
print("Wins: ", win)
print("Draws: ", draw)
print("Losses: ", loss)



            
    
