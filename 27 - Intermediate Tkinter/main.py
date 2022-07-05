import tkinter

window = tkinter.Tk()
window.title('Meu primeiro programa GUI!')
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text='Eu sou um Label', font=('Ariel', 15, 'bold'))
#my_label.pack(side='bottom')
my_label.pack()


# Alterando um componente criado
my_label['text'] = 'Novinho'
my_label.config(text='Aii novinho')


# Butões
def button_click():
    my_label['text'] = 'O botão foi clicado!!'


button = tkinter.Button(text='Click Me', command=button_click)
button.pack()

# Entry
def button_click_2():
    print(input.get())


button2 = tkinter.Button(text='Clique me 2', command=button_click_2)
button2.pack()
input = tkinter.Entry(width=30)
input.pack()


window.mainloop()