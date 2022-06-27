from consultaSQL import verifica_cpf

def valida_cpf(cpf_numeros):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in cpf_numeros if char.isdigit()]
    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False
    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def valida_cnpj(cnpj_numeros):
    pass

def valida_usuario_por_cpf(cpf_numeros):
    nome_usuario = verifica_cpf(cpf_numeros)
    if nome_usuario:
        return f'Olá {nome_usuario}'
    else:
        return 'Usuario nao encontrado'

print(valida_usuario_por_cpf('12133064e699'))


# # Controle simples de usuario via lista
# conta   =  ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
# senha   =  ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
# usuario =  ['Lucas', 'José', 'Pedro', 'Arthur', 'Livia', 'Maria', 'Fernada']

