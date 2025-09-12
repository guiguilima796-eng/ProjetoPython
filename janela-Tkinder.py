import tkinder as tk
from tkinder import ttk

largura = 300
altura = 100

lista = list()

def inserir(nome , email):
    tk.Text(root,f"seu nome é : {nome}")
    tk.Text(root,f"seu nome email é: {email}")
    lista.append(nome)
    tk.Text(root,"nome e email adicionados com sucesso!")
    print(nome)

root = tk.Tk()
root.title("Windows Tkinder ")
# root.resizable(False,False)
root.geometry('300x100')

tk.Label(root , text="Digite seu Nome:",bg ="yellow",fg="blue").pack(pady=5)
nome = tk.Entry(root, width=50).pack()
tk.Label(root , text="Digite seu Email:",bg ="yellow",fg="blue").pack()
email = tk.Entry(root, width=50).pack()
btinserir = tk.Button(root , text="inserir",bg="blue",fg="white",command=lambda:inserir(nome,email)).pack()
# lista = tk.Listbox(root,text="liata").pack()
root.mainloop()



# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()

# # create the application
# myapp = App()

# #
# # here are method calls to the window manager class
# #
# myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1000, 400)

# # start the program
# myapp.mainloop()