import pyfiglet, random

print(pyfiglet.figlet_format("Solar Game"))

#1 == Rock, 2 == Paper, 3 == Scissors
randomChoice = random.choice(["Rock", "Paper", "Scissors"])

playersChoice = input("Write Rock/Paper/Scissors: ")

print("Your opponent chooses " + randomChoice)
if randomChoice == "Rock":
    if playersChoice == "Rock":
        print("Tie!")
    elif playersChoice == "Paper":
        print("You Win!")
    else:
        print("You are loser and lox")
if randomChoice == "Paper":
    if playersChoice == "Rock":
        print("You are loser and lox")
    elif playersChoice == "Paper":
        print("Tie!")
    else:
        print("You are loser and lox")
if randomChoice == "Scissors":
    if playersChoice == "Rock":
        print("You are loser and lox")
    elif playersChoice == "Scissors":
        print("Tie!")
if not playersChoice in ["Rock", "Paper", "Scissors"]:print("lox wrong write and lose")
