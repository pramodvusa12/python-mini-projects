
#User_choice = The player selects:
#paper
#Scissors
#Computer_choice = The computer randomly selects one of the three options(not based on the user's choice).
#Result = Compare both choices and print whether the user wins, loses, or ties.
#Game Rules
#A. Rock
#Rock vs Rock → Tie
#rock vs Paper → Paper wins
#Rock vs Scissors → Rock wins
#B. Paper
#Paper vs Paper → Tie
#Paper vs Rock → Paper wins
#Paper vs Scissors → Scissors wins
#C. Scissors
#Scissors vs Scissors → Tie
#Scissors vs Rock → Rock wins
#Scissors vs Paper → Scissors wins

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your choice= Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)
print(f"user_choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same = Match Tie")

elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers rock = Computer wins")
        else:
             print("Rock smashes Scissor = user wins")

elif user_choice == "Paper":
        if comp_choice == Scissor:
            print("Scisssor cuts the paper = computer wins")
        else:
            print("Paper covers rock = User wins")

elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scisssor cuts the paper = computer wins")
        else:
            print("Rock smashes Scissor = user wins ")
    
    
    