"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.
"""

from random import randint

start = 1
end = 1000000000000000000
value = randint(start, end)

# print(value)
print("I'm thinking of a number between", start, 'and', end)

guess = None
counter = 0

current_start = start
current_end = end

while guess != value:
    guess = (current_start+current_end) // 2
    print(guess)
    counter += 1

    if guess < value:
        print('Higher.')
        current_start = guess
    elif guess > value:
        print('Lower.')
        current_end = guess

print(f"Congratulations! You guessed the right answer: {value}, in {counter} moves")