import random

possible_outcomes = ["R", "P", "S"]
dict_outcomes = { 
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

print("----The game is Rock, Paper, Scissors----")

#Player gets to choose
rock, paper, scissors = "R", "P", "S"

print("{0} for rock,\n {1} for paper,\n{2} for scissors ".format(rock, paper, scissors))


startOver = True
while startOver:
    #To get Computer's move
    cpu_move = random.choice(possible_outcomes)
    #Checking for invalids
    isNotValid = True
    while isNotValid:
        user_move = str(input("Please pick an option between R, P or S:  \n ").upper())
        player = dict_outcomes.get(user_move)
        cpu = dict_outcomes.get(cpu_move)
        if user_move in dict_outcomes.keys():
            isNotValid = False
            print("Player({0}) : CPU({1})".format(player, cpu))
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
    #when there is a tie, repeat
    if user_move == cpu_move:
        continue
    else:
        startOver = False
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


