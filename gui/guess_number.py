import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

secret = random.randint(1, 100)

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()


def check_guess():
    if int(guess.get()) == secret:
        result_text = "CORRECT!"
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    tkMessageBox.showinfo("Result", result_text)


window.setvar('secret', 10)
submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()

