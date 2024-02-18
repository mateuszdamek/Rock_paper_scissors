import random

r = "Rock"
p = "Paper"
s = "Scissors"

enemy_score = 0
score = 0
print("[1] - ROCK\n[2] - PAPER\n[3] - SCISSORS\n[4] - EXIT\n")

def show_results():
    print(f"Opponent's score: {enemy_score}")
    print(f"Your's score: {score}\n")

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
                show_results()
            elif(computer_choice == 1):
                print(f"Enemy's choice: {r}\nYour's choice: {r}\n")
                show_results()
            else:
                print(f"Enemy's choice: {s}\nYour's choice: {r}\n")
                score += 1
                show_results()
        case 2:
            if(computer_choice == 2):
                print(f"Enemy's choice: {p}\nYour's choice: {p}\n")
                show_results()
            elif(computer_choice == 1):
                print(f"Enemy's choice: {r}\nYour's choice: {p}\n")
                score += 1
                show_results()
            else:
                print(f"Enemy's choice: {s}\nYour's choice: {p}\n")
                enemy_score += 1
                show_results()
        case 3:
            if(computer_choice == 2):
                print(f"Enemy's choice: {p}\nYour's choice: {s}\n")
                score += 1
                show_results()
            elif(computer_choice == 1):
                print(f"Enemy's choice: {r}\nYour's choice: {s}\n")
                enemy_score += 1
                show_results()
            else:
                print(f"Enemy's choice: {s}\nYour's choice: {s}\n")
                show_results()
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

