from tkinter import *
from tkinter import messagebox


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
    site = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Erroooooor!!', message='All fields must be completed')
    else:
        is_ok = messagebox.askokcancel(title=site, message=f'Gostaria de salvar os dados:\n{email} \n{password}')

        if is_ok:
            with open('data.txt', 'a', encoding='utf-8') as f:
                text = f'{site} | {password} | {email}'
                f.write(f'{text}\n')

        clear_text()


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

website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

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
