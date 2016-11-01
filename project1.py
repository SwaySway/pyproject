import random
import time


def rps():
    print("Rock Paper Scissors")
    player = input("Enter either \"r\" for rock, \"p\" for paper, or \"s\" for scissors \n ")
    comp = ["rock", "paper", "scissors"]
    options = random.choice(comp)

    if player.lower() not in ('r', 's', 'p'):
        print("Please enter the correct input!")
    else:
        rps_result(player, options)
    main()


def rps_result(player, options):
    if player == "r" and options == "scissors":
        print("Computer choose \"scissors\" \n you Win!")
    if player == "p" and options == "rock":
        print("Computer choose \"rock\" \n you Win!")
    if player == "s" and options == "paper":
        print("Computer choose \"paper\" \n you Win!")
    if(player == "r" and options == "rock") or (player == "p" and options == "paper") or (player == "s" and options == "scissors"):
        print("It's a tie!")
    else:
        print("Computer choose " + options + " you lose!")


def number():
    num = input("Enter a number to see if it's a perfect number below: \n")
    mylist = factors(int(num))
    pointer = mylist[0]
    for i in range(1, len(mylist)-1):
        pointer = pointer + mylist[i]
    if(pointer == num):
        print(str(num) + " is a perfect number!")
    else:
        print(str(num) + " is a not perfect number!")
    main()

def factors(n):
    mylist = []
    for i in range(1, n+1):
        if n % i == 0:
            mylist.append(i)
    return mylist
    main()

def mcarlo():
    counter = 0
    ntrials = 10**7
    for i in range(ntrials):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        result = x**2 + y**2
        if result <= 1:
            counter += 1
        else:
            continue
    pi_estimate = 4 * counter/(1.0*ntrials)
    print("Trials")
    print(ntrials)
    print("Pi Estimation")
    print("%f" % pi_estimate)
    print("Time Taken")
    print(time.time())
    print("\n")
    main()

def error():
    print("Goodbye!")

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
    print("Press any other key to exit")
    choice = input("Enter a choice: \n")
    switch.get(str(choice), error)()


if __name__ == "__main__":
    main()