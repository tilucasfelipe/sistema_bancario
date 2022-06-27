from sqlite3 import *
from datetime import datetime
dataHora = datetime.now().strftime('%d-%m-%y %H:%M:%S')

def verificaSaldo(idUser):
    saldo = validaSaldo(idUser)
    if saldo:
        return saldo
    else:
        return False
    # if saldo:
    #     if saldo < 0:
    #         print('O saldo em conta é menor que o necessário para realizar a operação!')
    #         return False
    #     else:
    #         return saldo


def validaSaldo(idUser):
    import sqlite3 as db
    db = db.connect('banco.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT SALDO FROM SAL_SALDO WHERE CONTA = {idUser}")
    saldoBanco = cursor.fetchall()
    if saldoBanco:
        for saldo in saldoBanco:
            saldo = int(saldo[0]) / 100
        return saldo
    else:
        print('ERR')
        return False
    cursor.close()


def gravaSaque(idUser, valorDigitado, saldoInicial):
    import sqlite3 as db
    db = db.connect('banco.db')
    cursor = db.cursor()
    saldoFinal = saldoInicial - valorDigitado
    saldoFinal = int(saldoFinal * 100)
    try:
        cursor.execute(f'''insert into tra_transacao (tpo_id, conta, TRA_VALOR, TRA_VALOR_INICIAL, TRA_VALOR_FINAL,TRA_DATA) 
        values (1,{idUser},{valorDigitado*100},{saldoInicial*100},{saldoFinal},'{dataHora}')''')
        db.commit()
        print(f'Saque realizado com sucesso!')
    except DatabaseError as err:
        print(err)
        print('Erro ao adicionar o parametro')
    try:
        cursor.execute(f'update sal_Saldo set saldo = {saldoFinal} where conta = {idUser}')
        db.commit()
        print(f'Saldo final: {(saldoFinal):.2f}')
    except DatabaseError as err:
        print(err)
    cursor.close()


def gravaDeposito(idUser, valorDigitado, saldoInicial):
    # if valorDigitado == 0:
    #     print('Valor incorreto!')
    #     exit()
    import sqlite3 as db
    db = db.connect('banco.db')
    cursor = db.cursor()
    saldoFinal = saldoInicial + valorDigitado
    saldoFinal = int(saldoFinal*100)
    try:
        cursor.execute(f'''insert into tra_transacao (tpo_id, conta, TRA_VALOR, TRA_VALOR_INICIAL, TRA_VALOR_FINAL,TRA_DATA) 
        values (2,{idUser},{valorDigitado*100},{saldoInicial*100},{saldoFinal},'{dataHora}')''')
        db.commit()
        print(f'Depósito realizado com sucesso!')
    except DatabaseError as erro:
        db.rollback()
        db.close()
        print(erro)
    try:
        cursor.execute(f'update sal_Saldo set saldo = {saldoFinal} where conta = {idUser}')
        db.commit()
        cursor.close()
        print(f'Saldo final: {(saldoFinal):.2f}')
    except DatabaseError as erro:
        db.rollback()
        db.close()
        print(erro)


def realizaTransferencia():
    #TODO - Realizar interação entre contas de diferentes bancos
    pass

def consultaExtrato(idUser):
    import sqlite3 as db
    db = db.connect('banco.db')
    cursor = db.cursor()
    cursor.execute(f"""SELECT  TRA.TRA_ID, TRA.TRA_DATA, TRA.CONTA, TRA.TRA_VALOR, TRA.TRA_VALOR_FINAL/100, TPO.TPO_DESCRICAO,DAU.NOME
    FROM TRA_TRANSACAO TRA, DAU_DADOS_USUARIO DAU, TPO_TIPO_OPERACAO TPO, DAC_DADOS_CONTA DAC
    WHERE DAU.USUARIO_ID = DAC.USUARIO_ID AND TRA.CONTA = DAC.CONTA AND TRA.TPO_ID = TPO.TPO_ID AND
    TRA.CONTA = {idUser}""")
    relExtrato = cursor.fetchall()
    if relExtrato:
        print ('ID |   DATA TRANSACAO    |   CONTA   |  VALOR  |   SALDO    |    DESCRICAO   |         NOME        |')
        for extrato in relExtrato:
            print(f"""{extrato[0]}  |  {extrato[1]}  |  {extrato[2]}  |  {extrato[3]/100}  |   {extrato[4]/100}   |    {extrato[5]}    |  {extrato[6]}  |""")
        return extrato
    else:
        print('ERR')
        return False
    cursor.close()

"""SELECT  TRA.TRA_ID, TRA.TRA_DATA, TRA.CONTA, TRA.TRA_VALOR, TRA.TRA_VALOR_FINAL/100, TPO.TPO_DESCRICAO,DAU.NOME
    FROM TRA_TRANSACAO TRA, DAU_DADOS_USUARIO DAU, TPO_TIPO_OPERACAO TPO, DAC_DADOS_CONTA DAC
    WHERE 	DAU.USUARIO_ID = DAC.USUARIO_ID AND
    TRA.CONTA = DAC.CONTA AND
    TRA.TPO_ID = TPO.TPO_ID"""