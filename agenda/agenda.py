import os
import sqlite3
from sqlite3 import Error
import datetime

# Conexão
def conexaoBanco():
    caminho = "C:\\Users\\orion\\OneDrive\\Área de Trabalho\\projetos\\python\\agenda\\banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

def query(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com Sucesso")
        

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    vcon.close()
    return res


def menuPrincipal():
    os.system("cls")
    print("[1] - Inserir Novo Registro.")
    print("[2] - Deletar Registro.")
    print("[3] - Atualizar Registro")
    print("[4] - Consultar Registro por ID")
    print("[5] - Consultar Registro por Nome")
    print("[6] - Sair")

def verificarOpc(opc):
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultarId()
    elif opc == 5:
        menuConsultarNomes()
    elif opc == 6:
        menuSair()
    else:
        os.system("cls")
        print("opção inválida")
        os.system("pause")

def menuInserir():
    os.system("cls")
    data= datetime.date.today()
    nome = input("Digite o NOME: ")
    dia = int(input("Dia do  Nascimento: "))
    mes = int(input("Mês do Nascimento: "))
    ano = int(input("Ano do Nascimento: "))
    nascimento = datetime.date(ano,mes,dia)
    telefone = int(input("Digite o Telefone: "))
    email = input("Digite o E-mail: ")
    obs = input("Observaçôes: ")
    vsql=f'INSERT INTO tb_contatos (D_CADASTRO,N_CONTATO,D_NASCIMENTO,N_TELEFONE,EMAIL,T_OBS) VALUES("{data }","{nome}","{nascimento}","{telefone}","{email}","{obs}")'
    query(vcon,vsql)

def menuDeletar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser deletado: ")
    vsql = f'DELETE FROM tb_contatos WHERE ID_CONTATO={vid}'
    query(vcon,vsql)

def menuAtualizar():
    pass

def menuConsultarId():
    pass

def menuConsultarNomes():
    pass

def menuSair():
    os.system("cls")
    print("Programa Finalizado.")


vcon = conexaoBanco()
opcao = 0
while opcao != 6:
    menuPrincipal()
    opcao = int(input("Digite uma opção: "))
    verificarOpc(opcao)
    os.system("pause")


