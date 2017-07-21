# mega rock paper scissors
from random import randint


def leaderboard(score):
    while True:
        choice = raw_input("enter your name: ")
        if len(str(choice))<8:
            break
        else:
            print "that name is too long"
    with open("lboard.txt", "a") as textfile:
        textfile.write("\n['"+choice+"', "+ str(score) + "]")
    with open("lboard.txt", "r") as textfile:
        for i in range(9):
            print textfile.readline
def genAIChoice():
    choice = randint(1,3)
    if choice == 1:
        return "rock"
    if choice == 2:
        return "paper"
    if choice == 3:
        return "scissors"


def attempt():
    while True:
        choice = raw_input("go: ")
        if choice == "rock" or choice == "paper" or choice == "scissors":
            break
        print "that is not 'rock', 'paper' or 'scissors'"
    ai = genAIChoice()
    print "rock\npaper\nscissors\nyou - " + choice + " ai - " + str(ai)
    return int(result(choice,ai))


def result(player, ai):
    if player == ai:
        print "draw"
        return 0
    if player == "rock":
        if ai == "scissors":
            print "you win"
            return 1
        if ai == "paper":
            print "you lose"
            return -1
    if player == "paper":
        if ai == "rock":
            print "you win"
            return 1
        if ai == "scissors":
            print "you lose"
            return -1
    if player == "scissors":
        if ai == "paper":
            print "you win"
            return 1
        if ai == "rock":
            print "you lose"
            return -1
    else:
        return 0


def play():
    score = 0
    print "welcome to rock paper scissors, can you beat Alan the ai?\n -- five rounds -- \n"
    for i in range(1):
        score += int(attempt())
    print "you got: " + str(score)
    leaderboard(score)
play()

