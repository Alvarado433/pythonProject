from tkinter import messagebox

from Backend.crud.Crud import autenticar
from views.Administraçao import Administracao
class Autenticaçao:
    @staticmethod
    def autenticar(usuario, senha, label_error):
        if not usuario or not senha:
            messagebox.showwarning("Error", "Preencha os campos vazios")
            mensagem = "Preencha os campos vazios"
        elif not usuario:
            messagebox.showwarning("Error", "Preencha o campo nome")
            mensagem = "Preencha o campo nome"
        elif not senha:
            messagebox.showwarning("Error", "Preencha o campo senha")
            mensagem = "Preencha o campo senha"
        else:
            if autenticar(usuario, senha):
                messagebox.showinfo("success", "login efetuado com suceeso")
                mensagem = "login efetuado com suceeso"
                app = Administracao(usuario)
                app.run()
            else:
                messagebox.showinfo("success", "login ou senha incorretos")
                mensagem = "login ou senha incorretos"

        label_error.configure(text=mensagem)

