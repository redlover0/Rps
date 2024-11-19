# Welcoming player and giving instructions  
print("Welcome to Rock, Paper, Scissors\nWhen asked for choice please enter 'R' 'P' or 'S' ")

# getting players input
playerOneinput = input("player One select: R, P or S;")
playerTwoinput = input("player Two select: R, P or S;")

# compare players input to determain result either player one wins, player two wins or its a tie

if playerOneinput == "S":
    if playerTwoinput == "S":
        print("You have tied") # Nested statements 
    if playerTwoinput == "R":
        print("PLayer Two wins")
    if playerTwoinput == "P":
        print("Payer one wins!")

if playerTwoinput == "R":
    if playerOneinput == "S":
        print("Player Two wins")
    if playerOneinput == "R":
        print("You have a Tie")
    if playerOneinput == "P":
        print("Player One wins")

# print("player one input:" + playerOneinput + "\n"
#    "player one Two:" + playerTwoinput)

