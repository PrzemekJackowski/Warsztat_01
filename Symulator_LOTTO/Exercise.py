from random import randint

def lotto():
    numbers = []
    while len(numbers) != 6:
        checked = 0
        num = input("What's your num? ")
        num = int(num)
        if type(num) != int:
            print("It's not a num!")
        elif num not in range(1, 50):
            print("It's a wrong num!")
        else:
            checked = True
            if num in numbers:
                print("You gave that num before")
                checked = False
        if checked == True:
            numbers.append(num)

    print(sorted(numbers))
    random_num = []
    while len(random_num) < 7:
        d = randint(1, 50)
        if d not in random_num:
            random_num.append(d)
    print("LOTTO numbers: ", sorted(random_num))
    counter = 0
    for n in numbers:
        if n in random_num:
            counter += 1
    print("You hit ", counter, "numbers")


lotto()