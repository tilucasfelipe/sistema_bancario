from random import randint
estado = ''

def valida_cpf(digitos):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in digitos if char.isdigit()]

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
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def gerador_cpf():
    #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break


    #  Gera os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    #  Retorna o CPF como string
    result = ''.join(map(str, cpf))
    return result


opcao = int(input('''[1] Validar um CPF
[2] Gerar um CPF válido
Opção: '''))
if opcao == 1:
    cpf = input('Digite o CPF: ')
    if cpf[8] == '0':
        estado = 'RS'
    elif cpf[8] == '1':
        estado = 'DF'
    elif cpf[8] == '2':
        estado = 'RR'
    elif cpf[8] == '3':
        estado = 'CE'
    elif cpf[8] == '4':
        estado = 'RN'
    elif cpf[8] == '5':
        estado = 'BA'
    elif cpf[8] == '6':
        estado = 'MG'
    elif cpf[8] == '7':
        estado = 'RJ'
    elif cpf[8] == '8':
        estado = 'SP'
    elif cpf[8] == '9':
        estado = 'SC'
    if valida_cpf(cpf):
        print(f'CPF válido. \nEstado: {estado}')
    else:
        print('CPF inválido.')
elif opcao == 2:
    cpf = gerador_cpf()
    if cpf[8] == '0':
        estado = 'RS'
    elif cpf[8] == '1':
        estado = 'DF'
    elif cpf[8] == '2':
        estado = 'RR'
    elif cpf[8] == '3':
        estado = 'CE'
    elif cpf[8] == '4':
        estado = 'RN'
    elif cpf[8] == '5':
        estado = 'BA'
    elif cpf[8] == '6':
        estado = 'MG'
    elif cpf[8] == '7':
        estado = 'RJ'
    elif cpf[8] == '8':
        estado = 'SP'
    elif cpf[8] == '9':
        estado = 'SC'
    if valida_cpf(cpf):
        print(f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} \nEstado: {estado}')
else:
    print('Opção inválida!\nSaindo...')
