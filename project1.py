import random
import time

def rps():
    print("Rock Paper Scissors")
    player = raw_input("Enter either r for rock, p for paper, or s for scissors \n ")
    comp = ["rock", "paper", "scissors"]
    options = random.choice(comp)

    if player == "r" and options == "scissors":
        print("Computer choose \"scissors\" \n You Win!")
    if player == "p" and options == "rock":
        print("Computer choose \"rock\" \n You Win!")
    if player == "s" and options == "paper":
        print("Computer choose \"paper\" \n You Win!")
    if((player == "r" and options == "rock") or (player == "p" and options == "paper") or (player == "s" and options == "scissors")):
        print("It's a tie!")
    else:
        print ("Computer choose "+options+" You lose!")



def number():
    num = input("Enter a number to see if it's a perfect number below: \n")
    mylist = factors(int(num))
    pointer = mylist[0]
    for i in range(1, len(mylist)-1):
        pointer = pointer + mylist[i]
    if(pointer == num):
        print(str(num) + " is a perfect number!")

def factors(n):
    mylist = []
    for i in range(1, n+1):
        if n % i == 0:
            mylist.append(i)
    return mylist

def mcarlo():
    counter = 0
    ntrials = 10**6
    for i in range (ntrials):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        result = x**2 + y**2
        if result <= 1:
            counter += 1
        else:
            continue
    pi_estimate = 4 * counter/ntrials
    print("Estimated Pi: " + str(pi_estimate))
    print("Total Time taken: "+ str(time.time()))

def error():
    print("WRONG INPUT")

switch = {
    "1": rps,
    "2": number,
    "3": mcarlo,
}


def main():
    print("CS 299 Project 1")
    print("1) Rock Paper Scissors Game")
    print("2) Perfect Numbers")
    print("3) Monte Carlo")
    choice = input("Enter a choice: \n")
    switch.get(str(choice), error)()


if __name__ == "__main__":
    main()