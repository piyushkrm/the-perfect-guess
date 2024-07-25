'''
We are going to write a program that generates a random number and asks the user to
guess it.

If the player's guess is higher than the actual number, the program displays "Lower
number please". Similarly, if the user's guess is too low, the program prints "higher
number please" When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.

Hint: Use the random module.
'''

import random

computer = random.randint(1, 100)
user = -1

guesses = 0

while user != computer :
    user = int(input("Guess the number : "))

    if user > computer:
        print("Please lower number enter !")
        guesses += 1
        
    elif user < computer : 
        print("Please enter higher number !")
        guesses += 1

print(f"You have guessed the number {computer} correctly in {guesses} attempts")
