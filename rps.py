import time
## These are your Variables 
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player1 = ""
player2 = ""

# here we get into the fuctions where the user is able to say input yes or no which is a decision 

print("Welcome to Rock, Paper, Scissors")
time.sleep(2.5)
print("Would you like to know more about the name type Yes or No")
Yes = input("")


#  if else statements 

if Yes == "Yes":
    print("two players one after the other choose a hand gesture to represent rock, paper, or scissors, and the winner is determined by the following rules") 
    time.sleep(2) 
    print("Rock beats scissors: Rock is strong enough to break scissors")
    time.sleep(1)
    print('Scissors beats paper: Scissors can cut paper')
    time.sleep(1)  
    print('Paper beats rock: Paper can wrap around and cover rock')
elif Yes == "No":
    print("Let's play!") ## confirm tahat

Yes = input("") ## another input statement if we want it to wait

## This part is still in development, it runs everything at the same time and doesnt have a user inout option so you need to work on that
if player1 == "":
    print("First player, name yourself")  
    print( "your name is" + player1 + "are you sure")
    time.sleep(2)
    print("Second player, what would you like your name to be?")
    player2 = input("")

