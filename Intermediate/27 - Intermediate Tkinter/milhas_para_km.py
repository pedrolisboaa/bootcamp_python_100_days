import tkinter


def comando_botao():
    numero_de_fora = input.get()
    km = float(numero_de_fora) * 1.60934
    texto_tres.config(text=km)


# Criando a janela
janela = tkinter.Tk()
janela.title('Milhas para Km!')
janela.minsize(width=200, height=100)
janela.config(padx=10, pady=10)

# Entry ou Input
input = tkinter.Entry(width=15)
input.grid(column=1, row=0)
print(input.get())

# 1ª texto - Milhas
texto_um = tkinter.Label(text="Milhas")
texto_um.grid(column=2, row=0)

# 2ª texto - é igual a
texto_dois = tkinter.Label(text="é igual a")
texto_dois.grid(column=0, row=1)

# 3ª texto - onde vem a mudança
texto_tres = tkinter.Label(text='0')
texto_tres.grid(column=1, row=1)

# 3ª texto - KM
texto_quatro = tkinter.Label(text='Km')
texto_quatro.grid(column=2, row=1)

# Botão
botao = tkinter.Button(text='Calcular', command=comando_botao)
botao.grid(column=1, row=2)

# Aqui eu mantenho a janela aberta.
janela.mainloop()
