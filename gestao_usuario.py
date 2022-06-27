import consultaSQL

def cadastra_novo_usuario(nome, documento, dt_nascimento, nome_pai, nome_mae, sexo, endereco, telefone):
    pass

def exclui_usuario_existente(cpf_numeros):
    return (consultaSQL.exclui_usuario(cpf_numeros))

print(exclui_usuario_existente(123))