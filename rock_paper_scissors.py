import random

r = "Rock"
p = "Paper"
s = "Scissors"

enemy_score = 0
score = 0
print("[1] - ROCK\n[2] - PAPER\n[3] - SCISSORS\n[4] - EXIT\n")

while(True):
    try:
        choice = int(input("Choose your move: "))
    except ValueError:
        print("Only numbers are allowed.")
        continue

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
            break
        case other:
            print("Wrong choice!")
    
    if (score == 5):
        print("You win!")
        break
    elif (enemy_score == 5):
        print("You lose!")
        break

