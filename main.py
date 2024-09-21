from Backend.crud.Crud import autenticar
from views.inicio import InterfaceLogin
from views.Administraçao import Administracao
if __name__ == "__main__":
    app = InterfaceLogin()
    app.run()
    #criar_conexao()
    #autenticar("teste","teste")