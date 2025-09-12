import tkinter as tk

janela = tk.Tk()

janela.title("Minha Janela")

rotulo = tk.Label(janela, text="olá mundo!")

rotulo.pack()

janela.mainloop()