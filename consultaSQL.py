from sqlite3 import *
import sqlite3 as db
import datetime
from googletrans import Translator

db = db.connect('banco.db')
cursor = db.cursor()

tranlated = Translator()

def verificaSaldo(idUser):
    saldo = validaSaldo(idUser)
    if saldo:
        if validaSaldo(idUser) < 0:
            print('O saldo em conta é menor que o necessário para realizar a operação!')
            return False
        else:
            return saldo

def validaSaldo(idUser):
    cursor.execute(f'select saldo from sal_saldo where conta = {idUser}')
    saldoBanco = cursor.fetchall()
    if saldoBanco:
        for saldo in saldoBanco:
            saldo = int(saldo[0]) / 100
        return saldo
    else:
        print('ERR')
        return False
    cursor.close()

def gravaSaque(idUser,valorDigitado,saldoInicial):
    saldoFinal = saldoInicial - valorDigitado
    saldoFinal = int(saldoFinal * 100)
    print(saldoFinal)
    try:
        cursor.execute(f'''insert into tra_transacao (tpo_id, conta, TRA_VALOR, TRA_VALOR_INICIAL, TRA_VALOR_FINAL) values 
                    (1,{idUser},{valorDigitado},{saldoInicial},{saldoFinal})''')
        db.commit()
    except Exception as err:
        print(err)
        print('Erro ao adicionar o parametro')
    try:
        cursor.execute(f'update sal_Saldo set saldo = {saldoFinal} where conta = {idUser}')
        db.commit()
    except Exception as err:
        print(err)
    cursor.close()

def gravaDeposito(idUser,valorDigitado,saldoInicial):
    saldoFinal = saldoInicial + valorDigitado
    saldoFinal = int(saldoFinal * 100)
    print(saldoFinal)
    try:
        cursor.execute(f'''insert into tra_transacao (tpo_id, conta, TRA_VALOR, TRA_VALOR_INICIAL, TRA_VALOR_FINAL) values 
                    (2,{idUser},{valorDigitado},{saldoInicial},{saldoFinal})''')
        db.commit()
    except Exception as err:
        print(err)
        print('Erro ao adicionar o parametro')
    try:
        cursor.execute(f'update sal_Saldo set saldo = {saldoFinal} where conta = {idUser}')
        db.commit()
    except Exception as err:
        print(err)

    cursor.close()

def verifica_cpf(cpf_numeros):
    cursor.execute(f'select nome from dau_dados_usuario where n_documento = {cpf_numeros}')
    valida_cpf = cursor.fetchall()
    for cpf_validado in valida_cpf:
        cpf_validado = cpf_validado[0]

    if valida_cpf:
        return cpf_validado
    else:
        return False
    cursor.close()

def exclui_usuario(cpf_numeros):
    try:
        cursor.execute(f'SELECT USUARIO_ID FROM DAU_DADOS_USUARIO WHERE N_DOCUMENTO = {cpf_numeros};')
        usu_id = cursor.fetchall()
        if usu_id:
            for usuario_id in usu_id:
                    try:
                        cursor.execute(f'INSERT INTO LAU_LOG_AUDITORIA SELECT * FROM DAU_DADOS_USUARIO WHERE '
                                       f'USUARIO_ID = {usuario_id[0]};')
                        cursor.execute(f'DELETE FROM DAU_DADOS_USUARIO WHERE USUARIO_ID = {usuario_id[0]};')
                        db.commit()
                        msg = tranlated.translate(f'Usuario {cpf_numeros} excluido com sucesso!', src='pt'  , dest='ko').text
                        print(msg)
                    except Exception as error:
                        print(error)
        else:
            raise False
    except Exception as error:
        return ('Não foi possivel realizar a exclusao! \nRegistro não encontrado')
        #msg = tranlated.translate(f'Não foi possivel realizar a exclusao! \nRegistro não encontrado', src='pt', dest='ja').text
        #return (msg)
    cursor.close()