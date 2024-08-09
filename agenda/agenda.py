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

#commitar 
def query(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com Sucesso")
        
#Retorna consulta do BD
def consultar(sql):
    vcon = conexaoBanco()
    c=vcon.cursor()
    c.execute(sql)
    res = c.fetchall()
    vcon.close()
    return res

#display do menu
def menuPrincipal():
    os.system("cls")
    print("[1] - Inserir Novo Registro.")
    print("[2] - Deletar Registro.")
    print("[3] - Atualizar Registro")
    print("[4] - Consultar Registro por ID")
    print("[5] - Consultar Registro por Nome")
    print("[6] - Sair")

#verificar opção escolhida
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

#inserir novo registro
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
    vcon = conexaoBanco()
    query(vcon,vsql)
    vcon.close()

#Deletar registro
def menuDeletar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser deletado: ")
    vsql = f'DELETE FROM tb_contatos WHERE ID_CONTATO={vid}'
    vcon = conexaoBanco()
    query(vcon,vsql)
    vcon.close()

#atualizar registro
def menuAtualizar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser alterado: ")
    vcon = conexaoBanco()
    res = consultar(f'SELECT * FROM tb_contatos WHERE ID_CONTATO={vid}')
    res_nome = res[0][2]
    res_nasc = res[0][3]
    res_fone = res[0][4]
    res_email =res[0][5]
    res_obs = res[0][6]
    nome = input("Digite o NOME: ")
    telefone = int(input("Digite o Telefone ou 0: "))
    email = input("Digite o E-mail: ")
    obs = input("Observaçôes: ")
    if (len(nome)==0):
        nome = res_nome
    if( telefone ==0):
        telefone = res_fone
    if(len(email)==0):
        email = res_email
    if(len(obs)==0):
        obs = res_obs
    
    vsql=f'UPDATE tb_contatos SET N_CONTATO="{nome}",N_TELEFONE="{telefone}",EMAIL="{email}",T_OBS="{obs}" WHERE ID_CONTATO={vid} '
    query(vcon,vsql)
    vcon.close()

def menuConsultarId():
    pass

def menuConsultarNomes():
    pass

def menuSair():
    os.system("cls")
    print("Programa Finalizado.")


#Seção principal
opcao = 0
while opcao != 6:
    menuPrincipal()
    opcao = int(input("Digite uma opção: "))
    verificarOpc(opcao)
    os.system("pause")


