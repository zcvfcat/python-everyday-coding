import random

number = random.randint(1, 100)
print(f'ssh{number}')

while True:
    guess = int(input("Enter a guess: "))

    if guess == number:
        print(f'You got it right!')
        break

    elif guess < number:
        print(f'{guess} is too low; try again')
    else:
        print(f'{guess} is too high;')
