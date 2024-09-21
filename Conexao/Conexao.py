import sqlite3

def criar_conexao():
    # Conecta ao banco de dados (ou cria se não existir)
    conexao = sqlite3.connect("BancoBlind.db")

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Criar uma tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()

    #print("Banco de dados e tabela criados com sucesso.")
def obter_conexao():
    """Obtém uma conexão com o banco de dados."""
    conexao = sqlite3.connect("BancoBlind.db")
    return conexao
criar_conexao()