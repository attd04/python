from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# --------------------------- GENERATE PASSWORD ------------------------------- #


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbs = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_nums = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbs + password_nums
    random.shuffle(password_list)

    fin_password = "".join(password_list)
    password_input.insert(0, fin_password)
    pyperclip.copy(fin_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    web = website_input.get()
    mail = email_input.get()
    passw = password_input.get()
    new_data = {web: {"email": mail, "password": passw}}

    if len(web) == 0 or len(mail) == 0 or len(passw) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=web, message=f"Here are the entered details: \nEmail: {mail} "
                                              f"\nPassword: {passw} \nIs it ok to save?")
        if is_ok:
            with open('password_data.json', "aw") as data:
                json.dump(new_data, data, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg="white")

# labels
website_txt = Label(text='Website:', bg="white")
website_txt.grid(column=0, row=3)

email_txt = Label(text='Email / Username:', bg="white")
email_txt.grid(column=0, row=4)

password_txt = Label(text='Password:', bg="white")
password_txt.grid(column=0, row=5)

# canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# entries
website_input = Entry(width=35)
website_input.grid(column=1, row=3, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=4, columnspan=2)
email_input.insert(0, 'au_tiede@yahoo.com')

password_input = Entry(width=21)
password_input.grid(column=1, row=5)

# buttons
genpass_btn = Button(text='Generate Password', width=10, command=gen_pass)
genpass_btn.grid(column=2, row=5)

add_btn = Button(text='Add', width=20, command=save_data)
add_btn.grid(column=1, row=6, columnspan=2)

window.mainloop()
