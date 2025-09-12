import tkinter as tk

def mostrar_mensagem():
    nome = entrada.get()
    rotulo_resultado.config(text=f"Olá, {nome}!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter")
janela.geometry("300x150")

# Rótulo
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack()

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Botão
botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack()

# Rótulo para mostrar o resultado
rotulo_resultado = tk.Label(janela, text="")
rotulo_resultado.pack()

# Inicia a interface
janela.mainloop()
