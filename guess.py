import random
secret = random.randint(1, 20)  # stevilo med 1 in 20

# while guess != secret:
#
#     print('Poskusi uganiti skrito stevilo!')
#     guess = int(raw_input('Vnesi stevilo'))
#
#     if guess == secret:
#         print('Bravo!')
#         break
#     else:
#         print('Ponovno ugibaj')
lower_guess = 0
upper_guess = 20
guess = 10
for i in range(5):

    if secret > guess:
        lower_guess = guess
        print('Vecji od {guess}'.format(guess=guess))
        guess = guess + round((upper_guess - guess) / 2)
    elif secret == guess:
        print('Bravo')
        break
    elif secret < guess:
        upper_guess = guess
        print('Manjsi od {guess}'.format(guess=guess))

        guess = lower_guess + round((guess - lower_guess) / 2)


