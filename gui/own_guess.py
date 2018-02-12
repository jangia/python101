import Tkinter
import random
import tkMessageBox


class Secret:
    def __init__(self, val):
        self.value = val


window = Tkinter.Tk()
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

secret = Secret(random.randint(1, 100))

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()


def check_guess():
    if int(guess.get()) == secret.value:
        result_text = "CORRECT!"
        secret.value = random.randint(1, 5)
    elif int(guess.get()) > secret.value:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    tkMessageBox.showinfo("Result", result_text)


submit = Tkinter.Button(window, text="Submit", command=check_guess)
submit.pack()

window.mainloop()