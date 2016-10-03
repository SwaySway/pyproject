import random

def rps():
    print("Rock Paper Scissors")
    rps = ["rock", "paper", "scissors"]
    options = random.choice(rps)
    print(options)

    # player = input("Enter either \"rock\", \"paper\", or \"scissors\" ")
    #
    # if(player == "rock"):
    #     #something
    # if(player == "paper"):
    #     #something
    # if(player == "scissors"):
    #     #something






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

def carlo():
    print("sdfasdsdasdasdasdd")

def error():
    print("WRONG INPUT")

switch = {
    "1": rps,
    "2": number,
    "3": carlo,
}


def main():
    print("CS 299 Project 1")
    print ("1) Rock Paper Scissors Game")
    print ("2) Perfect Numbers")
    print ("3) Monte Carlo")
    choice = input("Enter a choice: \n")
    switch.get(str(choice), error)()




if __name__ == "__main__":
    main()