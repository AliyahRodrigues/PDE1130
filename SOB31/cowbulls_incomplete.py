import random

def compare_numbers(number, user_guess):
    cowbull=[0,0,0,0]
    for i in range(len(number)):
        if number[i]==user_guess[i]:
            cowbull[i]+=1
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number
guesses = 0

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1
    bull_count=sum(cowbullcount)
    cow_count=len(number)-bull_count

    print("You have "+ str(cow_count) + " cows, and " + str(bull_count) + " bulls.")

    if bull_count==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
        
