import random

answer = random.randint(1, 10)

def guess():
    n = int(input("Guess a number\n-> "))
    if n == answer:
        print(f"Correct! {n} was the correct answer.")
        
    elif n < answer:
        print("Too Low!")
        guess()
        
    elif n > answer:
        print("Too High!")
        guess()

guess()

print("Thanks for playing! Press enter to exit, or P to play again.")
a = input()
if a == "P" or a == "p":
    guess()
    answer = random.randint(1, 10)
