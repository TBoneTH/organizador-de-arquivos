import os
import threading
import customtkinter as ctk
from tkinter import filedialog

from organizador import organizar_arquivos

# Configuração visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()

app.title("Organizador de Arquivos")
app.geometry("500x460")

# Função da barra de progresso
def atualizar_barra(progresso):

    barra_progresso.set(progresso)

    porcentagem = int(progresso * 100)

    texto_progresso.configure(
        text=f"{porcentagem}%"
    )

    app.update_idletasks()

# Função do log
def adicionar_log(mensagem):

    log_box.configure(state="normal")
    log_box.insert("end", mensagem + "\n")
    log_box.see("end")
    log_box.configure(state="disabled")
    app.update_idletasks()

# Função do botão
def selecionar_pasta():

    pasta = filedialog.askdirectory(
        title="Selecione uma pasta"
    )

    if pasta and os.path.exists(pasta):

        # Mostra widgets
        barra_progresso.pack(pady=10)
        texto_progresso.pack()
        log_box.pack(pady=10, padx=20, fill="both")
        resultado.pack(pady=5)

        # Reseta
        barra_progresso.set(0)
        texto_progresso.configure(text="0%")
        resultado.configure(text="")
        log_box.configure(state="normal")
        log_box.delete("1.0", "end")
        log_box.configure(state="disabled")

        botao.configure(state="disabled")

        def tarefa():

            def log_callback(mensagem):
                app.after(0, lambda m=mensagem: adicionar_log(m))

            organizar_arquivos(
                pasta,
                atualizar_progresso=atualizar_barra,
                log_callback=log_callback
            )

            app.after(0, lambda: resultado.configure(
                text="✓ Arquivos organizados com sucesso!"
            ))
            app.after(0, lambda: botao.configure(state="normal"))

        threading.Thread(target=tarefa, daemon=True).start()

    else:

        resultado.pack(pady=10)
        resultado.configure(text="Nenhuma pasta selecionada.")

# Título
titulo = ctk.CTkLabel(
    app,
    text="Organizador de Arquivos",
    font=("Arial", 28)
)

titulo.pack(pady=30)

# Botão
botao = ctk.CTkButton(
    app,
    text="Selecionar Pasta",
    command=selecionar_pasta,
    width=200,
    height=40
)

botao.pack(pady=20)

# Barra de progresso
barra_progresso = ctk.CTkProgressBar(
    app,
    width=300
)

barra_progresso.set(0)

# Texto da porcentagem
texto_progresso = ctk.CTkLabel(
    app,
    text="0%"
)

# Log box
log_box = ctk.CTkTextbox(
    app,
    width=460,
    height=120,
    state="disabled",
    font=("Courier", 12)
)

# Texto resultado
resultado = ctk.CTkLabel(
    app,
    text=""
)

# Inicia app
app.mainloop()