import tkinter as tk
import os
# from PIL import Image,ImageTk

root = tk.Tk()
root.title("Login")
root.geometry("500x100")

script_dir = os.path.dirname(os.path.abspath(__file__))
caminho_imagem = os.path.join(script_dir, "imgs", "Key.png")

titulo = root.title("tela de Login")

label1 = tk.Label(root,text="Identificação do usuario",bg='lightblue',fg='white')
label1.config(font=('Arial',30))
label1.pack(fill='x',ipady=15)

image = tk.PhotoImage(file=caminho_imagem)
imagemMenor = image.subsample(8,8)

exibirImg = tk.Label(root,image=imagemMenor)
exibirImg.pack()

#frames 

frame_nome = tk.Frame(root)
frame_nome.pack(pady=10,ipady=5)
labelNome = tk.Label(frame_nome,text="Nome:")
labelNome.pack(side='left')

entry_nome_frame = tk.Frame(root)
entry_nome_frame.pack()
inputNome = tk.Entry(entry_nome_frame,width=50)
inputNome.pack(side='right')

frame_Label_senha = tk.Frame(root, bg="lightgreen")
frame_Label_senha.pack(pady=10,ipady=5)
labelSenha = tk.Label(frame_Label_senha,text="Senha:")
labelSenha.pack(side='left')

frameEntrysenha = tk.Frame(root)
frameEntrysenha.pack()
inputSenha = tk.Entry(frame_Label_senha,width=50)
inputSenha.pack(side='right')

frame_butao = tk.Frame(root)
frame_butao.pack()

butaoEntrar = tk.Button(frame_butao,text="Entrar",bg="blue",fg="white",)
butaoEntrar.pack(side='right')

check_frame = tk.Frame(root)
check_frame.pack()

check = tk.Checkbutton(check_frame)
check.pack()

root.mainloop()