from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator_password():
    import string
    from random import choice

    all = [*list(string.ascii_letters), *list(string.digits), *list(string.punctuation)]
    password = ''
    for _ in range(13):
        password += choice(all)

    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_data():
    site = website_input.get().upper()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {
        site: {
            'email': email,
            'password': password,
        }
    }

    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Erroooooor!!', message='All fields must be completed')
    else:
        try:
            with open('data.json', 'r') as f:
                # Reading old data
                data = json.load(f)
                # Updating old data with new dataa
                data.update(new_data)

            with open('data.json', 'w', encoding='utf-8') as f:
                # Saving update data
                json.dump(data, f, indent=4)


        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        finally:
            clear_text()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get().upper()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error!', message=f'No Data File found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website.capitalize(), message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error!', message=f'Does not exist {website.capitalize()}')






# ---------------------------- CLEAR TEXT ------------------------------- #
def clear_text():
    website_input.delete(0, END)
    email_user_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manage')
window.config(pady=20, padx=20, bg='WHITE')

# CANVAS
canvas = Canvas(width=200, height=200, bg='WHITE', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website
website_text = Label(text='Website:', bg='WHITE')
website_text.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

search = Button(text='Search', bg='WHITE', command=find_password)
search.grid(column=2, row=1)

# Email usermane
email_user = Label(text='Email/Username:', bg='WHITE')
email_user.grid(column=0, row=2)

email_user_input = Entry(width=36)
email_user_input.grid(column=1, row=2, columnspan=2)

# Password
password_text = Label(text='Password:', bg='WHITE')
password_text.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_button_generate = Button(text='Generate Password', bg='WHITE', command=generator_password)
password_button_generate.grid(column=2, row=3)

# Add
add_button = Button(text='Add', width=36, bg='WHITE', command=create_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
