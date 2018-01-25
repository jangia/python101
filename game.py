import random


def main():
    country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna"}

    while True:
        index = random.randint(0, 2)
        selected_country = country_capital_dict.keys()[index]

        guess = raw_input("What is the capital of %s? " % selected_country)

        check_guess(guess, country_capital_dict[selected_country])

        again = raw_input("Would you like to continue this game? (yes/no) ")
        if again == "no":
            break


def check_guess(guess, value):

    if guess == value:
        print 'Congrats!'
        return True
    else:
        print 'Ups! Wrong capital.'
        return False


if __name__ == '__main__':
    main()
