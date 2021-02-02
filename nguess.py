#Random Number Generator practice
# Does markdown work?

## Testing

import random

x, y = 1, 20

answer = random.randint(x, y)
print ("Testing Answer: ", answer)

#username = input("What do I call you? ")
guess = int(input("Guess a number from {} to {}: ".format(x, y)))


if guess == answer:
    print("That is correct. Congratulations!")
elif guess > answer:
    print("Wrong! Try a smaller number!")
elif guess < answer:
    print("Wrong! Think bigger!")


