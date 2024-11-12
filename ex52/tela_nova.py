import customtkinter as ctk
import aula_ctk
#funcao para criar a nova tela
def nova_tela(nome):
    janela_nova = ctk.CTk()

    janela_nova.geometry("500x500")

    texto2 = ctk.CTkLabel(janela_nova, text=f"Bem-Vindo {nome}")
    texto2.pack()
    def voltar():
        janela_nova.destroy()
        aula_ctk.main()

    btn2 = ctk.CTkButton(janela_nova, text="Voltar", command=voltar)
    btn2.pack()

    janela_nova.mainloop()