# Jared Jackson
# 11/1/19
# This will be a math game as the file name suggests
from random import *
user_answers = []
actual_answers = []


def math_game():
    sn = randint(1, 10)
    sn1 = randint(1, 10)
    sn2 = randint(1, 10)
    sn3 = randint(1, 10)
    print(f"What is {sn} + {sn1} - {sn2} * {sn3}?")
    a1 = input(">>>")
    if a1 == int:
        print("Lettuce continue")
    else:
        print("Can you enter a number please")
        a1 = input(">>>")
#        while a1 != int:
#            print('Can you enter a number?')
#            a1 = int(input(">>>"))
#            if a1 != int:
#                print("What are you doing?")
#
#            elif a1 == int:
#                print("Alright, lettuce continue")
#                break

    user_answers.append(int(a1))
    actual_answers.append(sn + sn1 - sn2 * sn3)
    print(a1)
    print("Was that hard? I felt like you struggled a bit.")

    print("Well this is the end. Would you like to try again?")
    again = input(">>>").title()
    if again == "Yes" or again == "Y":
        print("Alright, let's go again")
        math_game()

    elif again == "No" or again == "N":
        print("OKay, bye")
        exit()


print("Hello user, what is your name?")
name = input(">>>").title()
print(f"""Why hello there, {name}, you are going to be playing a game.
You have no say in the next few minutes of your life.
You will either have an easy time, of you will struggle, immensely...
That will be very enjoyable for me.
\nWould you say you good at math?""")
good = input(">>>").title()
if good == "Yes" or good == "Y":
    print("Good, that be a very useful asset to you.")

elif good == "No" or good == "N":
    print("Well, do you want to continue?")
    continu3 = input(">>>").title()
    if continu3 == "Yes" or continu3 == "Y":
        print("You're a good sport.")

    elif continu3 == "No" or continu3 == "N":
        n = randint(1, 100)
        if n <= 50:
            print("Alright, fine, I'll let you go.")
            exit()

        elif n >= 51:
            print("Alright I'll let you go.")
            print("\n" * 5)
            print("Just kidding, you can't go. You weren't in the lower percentile")
            print("Now let's continue.")

else:
    print("I didn't catch that, but we will continue anyways")

print("""Now, the rules for the game goes as follows.
You will be given different math problems.
You will have one attempt to guess each.
The first one will be an easy problem; a warm up if you will.
After that there will be 2 problem of each operation.
For example you will solve for 2 addition problems, 2 subtraction problems, 2 division problems and so on.""")
math_game()
