import tkinter as tk
import random
from tkinter import INSERT, END

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

window = tk.Tk()
window.title('Password generator')

tk.Button(
    window,
    text="Generate password",
    activebackground="black",
    activeforeground="white",
    width=20,
    command=lambda: generate_password()
).pack(pady=10)

text_password = tk.Text(
    window,
    width=50,
    height=6 / 2
)
text_password.pack()

tk.Button(
    window,
    text="Exit",
    width=20,
    activebackground="black",
    activeforeground="white",
    command=lambda: window.quit()
).pack(pady=10)


def generate_password():
    password_list = []

    for char in range(5):
        password_list.append(random.choice(letters))

    for char in range(5):
        password_list.append(random.choice(numbers))

    for char in range(5):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password = "".join(password_list)
    text_password.delete('1.0', END)
    text_password.insert(INSERT, password)


window.mainloop()
