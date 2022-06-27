from gravaOperacao import *

def saque(valorDigitado, idUser):
    saldo = (verificaSaldo(idUser))

    if saldo != 0: #and saldo >= valorDigitado:
        gravaSaque(idUser, valorDigitado, saldo)
    else:
        print(f'Erro ao realizar a operação de saque!\nSaldo {saldo :.2f} insulficiente!')


def deposito(valorDigitado, idUser):
    saldo = (verificaSaldo(idUser))
    gravaDeposito(idUser, valorDigitado, saldo)


def extrato(idUser):
    extrato = consultaExtrato(idUser)


extrato('2121001')
