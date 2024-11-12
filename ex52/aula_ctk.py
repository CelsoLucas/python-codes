import customtkinter as ctk
import tela_nova as tn


def main():
    def abrir_tela():
        nome = input1.get()
        janela.destroy()
        tn.nova_tela(nome)

    #Criando uma janela
    janela = ctk.CTk()

    #Aumentando o tamanho da tela
    janela.geometry("500x500")

    #Mudando a cor da tela
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    #Criando uma Label(Texto)
    txt1 = ctk.CTkLabel(janela, text="Bem-Vindo")
    txt1.pack()
    txt1.place(x=225, y=100)

    #Criando um input
    input1 = ctk.CTkEntry(janela, placeholder_text="Digite seu nome")
    input1.pack()
    input1.place(x=190, y=150)

    #Criando um botão
    btn1 = ctk.CTkButton(janela, text="Entrar", command=abrir_tela)
    btn1.pack() 
    btn1.place(x=190, y=190)

    janela.mainloop()
if __name__ == "__main__":
    main()