import random

possible_outcomes = ["R", "P", "S"]
print("----The game is Rock, Paper, Scissors---- ")

#Player gets to choose
rock = "R"
paper = "P"
scissors = "S"

print("{0} for rock,\n {1} for paper,\n{2} for scissors ".format(rock, paper, scissors))


#To get Computer's move
cpu_move = random.choice(possible_outcomes)

isNotValid = True
while isNotValid:
    user_move = str(input("Please pick an option between R, P or S:  \n ").upper())
    if user_move in possible_outcomes:
        isNotValid = False
        print("Player({0}) : CPU({1})".format(user_move, cpu_move))
    elif user_move == cpu_move:
        continue
    else:
        print("Invalid Input!")
        continue
    
    def play_game(user_move, cpu_move):
        #Rules to determine winner
        if (user_move == "R" and cpu_move == "S" or user_move == "S" and cpu_move =="R"):
            return "Rock beats Scissors"
        elif (user_move == "P" and cpu_move == "R" or user_move == "R" and cpu_move == "P"):
            return "Paper beats Rock"
        elif (user_move == "S" and cpu_move == "P" or user_move == "P" and cpu_move == "S"):
            return "Scissors beats Paper"
        else:
            return "It's a tie!"
    print(play_game(user_move, cpu_move))

    def check_moves(user_move, cpu_move):
        #Who won?
        user_wins = "You win!"
        comp_wins = "Computer wins!"
        if (user_move == "R" and cpu_move == "S") or (user_move == "P" and cpu_move == "R") or (user_move == "S" and cpu_move == "P"):
            return user_wins
        elif (user_move == "S" and cpu_move == "R") or (user_move == "R" and cpu_move == "P") or (user_move == "P" and cpu_move == "S"):
            return comp_wins
        else:
            return " "
    print(check_moves(user_move, cpu_move))


print("-----Thanks for playing-----")

end_game = str(input("Press Enter to exit"))       


