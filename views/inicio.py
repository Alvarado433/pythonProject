import customtkinter as ctk
from Backend.Autenticaçao import Autenticaçao

class InterfaceLogin:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Blind Óculos Inteligente")
        self.window.geometry("450x300")
        self.window.resizable(False, False)

        # Painel lateral
        self.panel = ctk.CTkFrame(self.window, width=154, height=261, corner_radius=0, fg_color="gray")
        self.panel.pack(side="left", fill="y")

        self.label_nome = ctk.CTkLabel(self.panel, text="Blind", text_color="white", font=("Arial", 24))
        self.label_nome.place(relx=0.5, rely=0.5, anchor="center")

        # Labels e entradas (ajustados para a direita)
        self.label_usuario = ctk.CTkLabel(self.window, text="Usuário:")
        self.label_usuario.place(relx=0.65, y=80, anchor="center")

        self.entry_usuario = ctk.CTkEntry(self.window, width=200)
        self.entry_usuario.place(relx=0.65, y=105, anchor="center")

        self.label_senha = ctk.CTkLabel(self.window, text="Senha:")
        self.label_senha.place(relx=0.65, y=140, anchor="center")

        self.entry_senha = ctk.CTkEntry(self.window, width=200, show='*')
        self.entry_senha.place(relx=0.65, y=165, anchor="center")

        self.button_login = ctk.CTkButton(self.window, text="Login", command=self.login)
        self.button_login.place(relx=0.65, y=210, anchor="center")

        # Mensagem de erro
        self.label_error = ctk.CTkLabel(self.window, text="", text_color="red")
        self.label_error.place(relx=0.65, y=240, anchor="center")

    def login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Chama o método estático passando a label
        Autenticaçao.autenticar(usuario, senha, self.label_error)

    def run(self):
        self.window.mainloop()



