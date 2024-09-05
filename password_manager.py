from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )
    
    random.shuffle(password_list)
    new_password = ''.join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, new_password)
    pyperclip.copy(new_password)  # Copy password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message='Please do not leave any fields empty.')
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nSave?")
    
    if is_ok:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_password():
    website = web_entry.get()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')
        return

    if website in data:
        email = data[website]['email']
        password = data[website]['password']
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title='Error', message=f'No details for {website} exist.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas for logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
pass_label = Label(text='Password:')
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'unkoow@outlook.com')
pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

# Buttons
pass_button = Button(text='Generate Password', command=generate_password)
pass_button.grid(row=3, column=2)
add_button = Button(text='Add', width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search', width=15, command=search_password)
search_button.grid(row=1, column=2)

# Start the Tkinter event loop
window.mainloop()
