from operacaoBancaria import *
import validaUsuario

# Validação da usuario e senha via arquivo de configuração - DESABILITADO
# conta = input("Digite a sua conta: \n")
#
# loginAltorizado = False
# while loginAltorizado == False:
#     for contaUsuario in range(len(validaUsuario.conta)):
#         if validaUsuario.conta[contaUsuario] == conta:
#             senha = input("Digite a sua senha: \n")
#             if validaUsuario.senha[contaUsuario] == senha:
#                 print(f'Login autorizado para {validaUsuario.usuario[contaUsuario]}!')
#                 loginAltorizado = True
#     if loginAltorizado == False:
#         conta = input("Erro ao validar as informações de acesso! Digite novamente a conta:\n")
# Contador de erros de validação da opção de operação que será executada iniciada por 0
erro = int(0)

# Solicitação da operação desajada utilizando os numeros 1 ou 2. O contador de erros inicia em 0
choiceOperation = int(input(
    "[1] Saque\n"
    "[2] Depósito\n"))

# É realizada uma validação dos campos digitados e caso seja diferente do intervalo, será retornado um erro
while choiceOperation < 1 or choiceOperation > 2:
    # Limitação dos erros de digitação em 3
    if erro > 1:
        print("Quantidade de erros máximos atingidos! \nEncerrando...")
        exit()
    # Acréscimo de erro
    erro += 1
    print(f"Seleção inválida! Erros: {erro}. \nTente novamente: ")
    choiceOperation = int(input(
        "1) Saque\n"
        "2) Depósito\n"))



if choiceOperation == 1:
    valorDigitado = float(input("Digite o valor do saque: \n"))
    while valorDigitado <= 0:
        valorDigitado = float(input("Valor deve ser positivo! Digite novamente ou ctrl+c para sair:\n"))
    saque(valorDigitado, '2121001')
elif choiceOperation == 2:
    valorDigitado = float(input("Digite o valor do deposito: \n"))
    while valorDigitado <= 0:
        valorDigitado = float(input("Valor deve ser positivo! Digite novamente ou ctrl+c para sair:\n"))
    deposito(valorDigitado, '2121001')
