def user_choice():
    choices = ["too small", "too big", "you won"]
    while True:
        answer = input().lower()
        if answer in choices:
            break
        print("Input is not in ['too small', 'too big', 'you won']")
    return answer
def com_choice():
    print("Choose number between 0 and 1000!")
    print("Press 'Enter' to continue")
    input()
    minimal = 0
    maximal = 1000
    answer = ""
    while answer != "you won":
        com_choice = (maximal - minimal) // 2 + minimal
        print(f"Your number is: {com_choice}")
        answer = user_choice()
        if answer == "too big":
            maximal = com_choice
        elif answer == "too small":
            minimal = com_choice

    print("Hurray! I got you!")

if __name__ == '__main__':
    com_choice()
