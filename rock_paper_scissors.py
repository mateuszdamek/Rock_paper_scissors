import random

r = "Rock"
p = "Paper"
s = "Scissors"

choice = int(input("[1] - ROCK\n[2] - PAPER\n[3] - SCISSORS\n[4] - EXIT\nChoose your move: "))
enemy_score = 0
score = 0

while(choice != 4 and score < 5 and enemy_score < 5):

    computer_choice = random.randrange(1, 4)
    match choice:
        case 1:
            if(computer_choice == 2):
                print(f"Enemy's choice: {p}\nYour's choice: {r}\n")
                enemy_score += 1
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
            elif(computer_choice == 1):
                print(f"Enemy's choice: {r}\nYour's choice: {r}\n")
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
            else:
                print(f"Enemy's choice: {s}\nYour's choice: {r}\n")
                score += 1
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
        case 2:
            if(computer_choice == 2):
                print(f"Enemy's choice: {p}\nYour's choice: {p}\n")
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
            elif(computer_choice == 1):
                print(f"Enemy's choice: {r}\nYour's choice: {p}\n")
                score += 1
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
            else:
                print(f"Enemy's choice: {s}\nYour's choice: {p}\n")
                enemy_score += 1
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
        case 3:
            if(computer_choice == 2):
                print(f"Enemy's choice: {p}\nYour's choice: {s}\n")
                score += 1
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
            elif(computer_choice == 1):
                print(f"Enemy's choice: {r}\nYour's choice: {s}\n")
                enemy_score += 1
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
            else:
                print(f"Enemy's choice: {s}\nYour's choice: {s}\n")
                print(f"Opponent's score: {enemy_score}")
                print(f"Your's score: {score}\n")
        case 4:
            print("EXIT.")
        case other:
            print("Wrong choice!")
    
    if (score == 5):
        print("You win!")
        break
    elif (enemy_score == 5):
        print("You lose!")
        break
    else:
        choice = int(input("Choose your move: "))
