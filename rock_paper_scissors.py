import random

choices = ["Rock", "Paper", "Scissors"]
enemy_score = 0
score = 0

def show_results():
    print(f"Opponent's score: {enemy_score}")
    print(f"Your's score: {score}\n")

def check_results(player_s, computer_s, sc, esc):
    print(f"Your's choice: {choices[player_s - 1]}\nEnemy's choice: {choices[computer_s]}\n")
    global enemy_score 
    enemy_score += esc
    global score 
    score += sc
    show_results()

print("[1] - ROCK\n[2] - PAPER\n[3] - SCISSORS\n[4] - EXIT\n")

while(True):
    try:
        p_choice = int(input("Choose your move: "))
    except ValueError:
        print("Only numbers are allowed.")
        continue

    c_choice = random.randrange(0, 3)
    match p_choice:
        case 1:
            if(c_choice == 2):
                check_results(p_choice, c_choice, 1, 0)
            elif(c_choice == 1):
                check_results(p_choice, c_choice, 0, 1)
            else:
                check_results(p_choice, c_choice, 0, 0)

        case 2:
            if(c_choice == 2):
                check_results(p_choice, c_choice, 0, 1)

            elif(c_choice == 1):
                check_results(p_choice, c_choice, 0, 0)
            else:
                check_results(p_choice, c_choice, 1, 0)

        case 3:
            if(c_choice == 2):
                check_results(p_choice, c_choice, 0, 0)
            elif(c_choice == 1):
                check_results(p_choice, c_choice, 1, 0)
            else:
                check_results(p_choice, c_choice, 0, 1)

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

