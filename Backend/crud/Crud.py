from Conexao.Conexao import obter_conexao

def autenticar(usuario, senha):
    conexao = obter_conexao()
    cursor = conexao.cursor()

    # Consultar o usuário no banco de dados
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()  # Obtém a primeira linha que corresponde à consulta

    conexao.close()  # Fecha a conexão

    return resultado is not None  # Retorna True se a autenticação for bem-sucedida, caso contrário, False
