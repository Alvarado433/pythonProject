import customtkinter as ctk

class Administracao:
    def __init__(self, usuario):
        self.usuario = usuario
        ctk.set_appearance_mode("dark")  # Modo escuro
        ctk.set_default_color_theme("blue")  # Tema azul

        self.window = ctk.CTk()
        self.window.title("Blind Óculos Inteligente")
        self.window.geometry("500x350")
        self.window.resizable(False, False)

        # Painel esquerdo
        self.panel_left = ctk.CTkFrame(self.window, width=150, corner_radius=0, fg_color="#2E2E2E")
        self.panel_left.pack(side="left", fill="y")

        self.label_nome = ctk.CTkLabel(self.panel_left, text="Administração", text_color="white", font=("Arial", 16))
        self.label_nome.pack(pady=(20, 0))

        self.button_cadastrar = ctk.CTkButton(self.panel_left, text="Cadastrar Usuário", command=self.show_cadastrar)
        self.button_cadastrar.pack(pady=(10, 10), padx=20)

        self.button_mapear = ctk.CTkButton(self.panel_left, text="Mapear Área", command=self.show_mapear)
        self.button_mapear.pack(pady=(10, 10), padx=20)

        self.button_treinar = ctk.CTkButton(self.panel_left, text="Treinar Objeto", command=self.show_treinar)
        self.button_treinar.pack(pady=(10, 10), padx=20)

        self.button_treinar = ctk.CTkButton(self.panel_left, text="Ligar camera", command=self.show_treinar)
        self.button_treinar.pack(pady=(10, 10), padx=20)

        self.button_treinar = ctk.CTkButton(self.panel_left, text="Cadastra imagem", command=self.show_treinar)
        self.button_treinar.pack(pady=(10, 10), padx=20)

        self.button_sair = ctk.CTkButton(self.panel_left, text="Sair", command=self.window.quit)
        self.button_sair.pack(pady=(10, 20), padx=20)

        self.label_usuario = ctk.CTkLabel(self.panel_left, text=f"Usuário: {self.usuario}", text_color="white")
        self.label_usuario.pack(pady=(10, 0))

        # Painel direito
        self.panel_right = ctk.CTkFrame(self.window, width=350, corner_radius=0, fg_color="black")
        self.panel_right.pack(side="right", fill="both", expand=True)

        self.label_bem_vindo = ctk.CTkLabel(self.panel_right, text="Bem-vindo à Administração do Óculos", font=("Arial", 16))
        self.label_bem_vindo.pack(pady=(20, 20))

        self.label_instrucoes = ctk.CTkLabel(self.panel_right, text="Selecione uma opção à esquerda.", font=("Arial", 12))
        self.label_instrucoes.pack(pady=(0, 20))

    # Métodos para mostrar as seções da interface
    def show_cadastrar(self):
        self.clear_right_panel()
        self.label_bem_vindo.configure(text="Cadastrar Usuário")
        self.label_instrucoes.configure(text="Insira os dados do usuário.")

        self.entry_nome = ctk.CTkEntry(self.panel_right, placeholder_text="Nome")
        self.entry_nome.pack(pady=(10, 10))

        self.entry_senha = ctk.CTkEntry(self.panel_right, placeholder_text="Senha", show="*")
        self.entry_senha.pack(pady=(10, 10))

        self.button_confirmar = ctk.CTkButton(self.panel_right, text="Confirmar", command=self.confirmar_cadastro)
        self.button_confirmar.pack(pady=(10, 20))

    def show_mapear(self):
        self.clear_right_panel()
        self.label_bem_vindo.configure(text="Mapear Área")
        self.label_instrucoes.configure(text="Insira os dados para mapear a área.")

        self.entry_area = ctk.CTkEntry(self.panel_right, placeholder_text="Área")
        self.entry_area.pack(pady=(10, 10))

        self.button_mapear_area = ctk.CTkButton(self.panel_right, text="Mapear", command=self.mapear_area)
        self.button_mapear_area.pack(pady=(10, 20))

    def show_treinar(self):
        self.clear_right_panel()
        self.label_bem_vindo.configure(text="Treinar Objeto")
        self.label_instrucoes.configure(text="Insira os dados para treinar o objeto.")

        self.entry_objeto = ctk.CTkEntry(self.panel_right, placeholder_text="Objeto")
        self.entry_objeto.pack(pady=(10, 10))

        self.button_treinar_objeto = ctk.CTkButton(self.panel_right, text="Treinar", command=self.treinar_objeto)
        self.button_treinar_objeto.pack(pady=(10, 20))

    def clear_right_panel(self):
        for widget in self.panel_right.winfo_children():
            widget.destroy()

        self.label_bem_vindo = ctk.CTkLabel(self.panel_right, text="", font=("Arial", 16))
        self.label_bem_vindo.pack(pady=(20, 20))

        self.label_instrucoes = ctk.CTkLabel(self.panel_right, text="", font=("Arial", 12))
        self.label_instrucoes.pack(pady=(0, 20))

    def confirmar_cadastro(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()
        # Lógica para cadastrar o usuário
        print(f"Cadastrando usuário: {nome}")

    def mapear_area(self):
        area = self.entry_area.get()
        # Lógica para mapear a área
        print(f"Mapeando área: {area}")

    def treinar_objeto(self):
        objeto = self.entry_objeto.get()
        # Lógica para treinar o objeto
        print(f"Treinando objeto: {objeto}")

    def run(self):
        self.window.mainloop()
