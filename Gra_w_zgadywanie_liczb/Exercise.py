from random import randint

guessed = False
rnd = randint(1, 100)

while not guessed:
    try:
        str_num = input("Guess the number!: ")
        num = int(str_num)
        if num == rnd:
            print("You win!")
            guessed = True
        elif num < rnd:
            print("To small!")
        else:
            print("To big!")
    except ValueError:
        print("It's not a number!")
