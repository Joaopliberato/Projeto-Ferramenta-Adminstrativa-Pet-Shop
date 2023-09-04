import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os
from datetime import datetime


def registrar_servico():
    subprocess.Popen(["venv\\Scripts\\python.exe", "registroserv.py"])
    janela.destroy()


def cadastrar_cliente():
    subprocess.Popen(["venv\\Scripts\\python.exe", "registrocliente.py"])
    janela.destroy()


def visualizar_clientes():
    os.startfile("petshopclientes_data.xlsx")


def update_clock():
    current_time = datetime.now().strftime("%H:%M")
    clock_label.configure(text=current_time)
    janela.after(60000, update_clock)  # Atualiza a cada minuto (60000 milissegundos)


def update_date():
    current_date = datetime.now().strftime("%d/%m/%Y")
    date_label.configure(text=current_date)
    janela.after(86400000, update_date)  # Atualiza a cada dia (86400000 milissegundos)


# Criar janela principal
janela = tk.Tk()
janela.title("Ferramenta Administrativa - Aroa Pet Shop")
janela.geometry("800x600")


# Configurar cores
cor_fundo = "#1c1c1c"  # Preto
cor_barra_lateral = "#222222"  # Cinza escuro
cor_botao = "#ff9914"  # Laranja
cor_texto = "white"  # Branco
cor_retangulo = "#1c1c1c"  # Um pouco mais escuro que a barra lateral
cor_faixa = "#ff9914"  # Cor da faixa


# Configurar fundo da janela
janela.configure(bg=cor_fundo)


# Carregar e redimensionar a imagem de fundo
imagem_original = Image.open("pic/degrade.jpg")
tamanho_desejado = (800, 600)  # Tamanho desejado da imagem
imagem_redimensionada = imagem_original.resize(tamanho_desejado)
imagem = ImageTk.PhotoImage(imagem_redimensionada)


# Adicionar imagem de fundo como Label
label_fundo = tk.Label(janela, image=imagem)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


# Criar barra lateral
frame_lateral = tk.Frame(janela, width=150, bg=cor_barra_lateral)
frame_lateral.pack(side="left", fill="y")


# Carregar e redimensionar a imagem da barra lateral
imagem_original = Image.open("pic/gdp.png")
tamanho_desejado = (160, 160)  # Tamanho desejado da imagem
imagem_redimensionada = imagem_original.resize(tamanho_desejado)
imagem_barra_lateral = ImageTk.PhotoImage(imagem_redimensionada)

# Adicionar imagem acima do texto
label_imagem = tk.Label(frame_lateral, image=imagem_barra_lateral, bg=cor_barra_lateral)
label_imagem.pack(pady=10)

# Adicionar texto no topo da barra lateral
texto_topo = tk.Label(frame_lateral, text="Painel de Controle", bg=cor_barra_lateral, fg=cor_texto,
                      font=("Montserrat", 12, "bold"))
texto_topo.pack(pady=10)

# Criar retângulo em torno do texto "Seja Bem Vindo!"
frame_retangulo = tk.Frame(frame_lateral, bg=cor_retangulo)
frame_retangulo.pack(pady=10, padx=5)

# Adicionar texto dentro do retângulo
texto_inferior = tk.Label(frame_retangulo, text="Aroa Pet Shop 2023™", bg=cor_retangulo, fg=cor_texto,
                          font=("Montserrat", 12, "bold"))
texto_inferior.pack(pady=5)


def criar_botao_lateral(texto, comando, width=None):
    # Criar frame para o botão
    frame_botao = tk.Frame(frame_lateral, bg=cor_barra_lateral)
    frame_botao.pack(fill="x", padx=5)

    # Criar faixa vertical à esquerda do botão
    faixa_vertical = tk.Frame(frame_botao, width=3, bg=cor_faixa)
    faixa_vertical.pack(side="left", fill="y")

    # Criar botão

    botao = tk.Button(frame_botao, text=texto, bg=cor_barra_lateral, fg=cor_botao, font=("Montserrat", 12, "bold"), bd=0,
                      activebackground=cor_barra_lateral, activeforeground=cor_botao, command=comando, width=width)
    botao.pack(pady=5, padx=5, fill="x")



criar_botao_lateral("Registrar Serviço", registrar_servico, width=15)
criar_botao_lateral("Cadastrar Cliente", cadastrar_cliente, width=15)
criar_botao_lateral("Visualizar Clientes", visualizar_clientes, width=15)


clock_label = tk.Label(frame_lateral, text="", bg=cor_barra_lateral, fg=cor_texto,
                       font=("Montserrat", 12, "bold"))
clock_label.pack(pady=10)
update_clock()  # Iniciar atualização do relógio


date_label = tk.Label(frame_lateral, text="", bg=cor_barra_lateral, fg=cor_texto,
                      font=("Montserrat", 12, "bold"))
date_label.pack(pady=10)
update_date()  # Iniciar atualização da data


janela.mainloop()