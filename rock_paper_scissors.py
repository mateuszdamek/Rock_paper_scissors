import random

choices = ["Rock", "Paper", "Scissors"]
enemy_score = 0
score = 0

def show_results():
    print(f"Opponent's score: {enemy_score}")
    print(f"Your's score: {score}\n")

def check_results(player_s, computer_s):
    print(f"Your's choice: {choices[player_s - 1]}\nEnemy's choice: {choices[computer_s]}\n")

print("[1] - ROCK\n[2] - PAPER\n[3] - SCISSORS\n[4] - EXIT\n")

while(True):
    try:
        player_choice = int(input("Choose your move: "))
    except ValueError:
        print("Only numbers are allowed.")
        continue

    computer_choice = random.randrange(0, 3)
    match player_choice:
        case 1:
            if(computer_choice == 2):
                check_results(player_choice, computer_choice)
                score += 1
                show_results()
            elif(computer_choice == 1):
                check_results(player_choice, computer_choice)
                enemy_score += 1
                show_results()
            else:
                check_results(player_choice, computer_choice)
                show_results()
        case 2:
            if(computer_choice == 2):
                check_results(player_choice, computer_choice)
                enemy_score += 1
                show_results()
            elif(computer_choice == 1):
                check_results(player_choice, computer_choice)
                show_results()
            else:
                check_results(player_choice, computer_choice)
                score += 1
                show_results()
        case 3:
            if(computer_choice == 2):
                check_results(player_choice, computer_choice)
                show_results()
            elif(computer_choice == 1):
                check_results(player_choice, computer_choice)
                score += 1
                show_results()
            else:
                check_results(player_choice, computer_choice)
                enemy_score += 1
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

