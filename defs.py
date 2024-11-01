import verificacao
import os
import sys


class ReturnToMain(Exception):
    pass

def limpar_tela():
    os.system('cls')
    
def voltar_esc():
    voltar = str(input("Voltar [S]:  ")).lower()
    if voltar == 's':
        limpar_tela()
        raise ReturnToMain()
    
def cadastro(memoria):
    while True:
        limpar_tela()
        nome = verificacao.nome_v()
        senha = verificacao.senha_v()
        idade = verificacao.idade_v()
        cpf = verificacao.cpf_v()
        cidade = verificacao.cidade_v()
        rua = verificacao.rua_v()
        cidade = verificacao.cidade_v()
        
        
        # Armazenando dados no dicionário
        memoria[(nome, senha)] = {
            "idade": idade,
            "cidade": cidade,
        }
    
        continuar = input("Deseja adicionar outra pessoa? (S/N): ").lower()
        if continuar == 'n':
            limpar_tela()
            print("Dados cadastrados.")
            raise ReturnToMain()
        
def dados_usuario(memoria):
    while True:
        nome_usuario = verificacao.nome_dados()
        senha_usuario = verificacao.senha_dados()
        
        if (nome_usuario, senha_usuario) in memoria:
            limpar_tela()
            dados = memoria[(nome_usuario, senha_usuario)]
            print(f"Nome: {nome_usuario} \nIdade: {dados['idade']}, \nCidade: {dados['cidade']}")
            return nome_usuario, senha_usuario
        else:
            print("Usuário não encontrado.")
        voltar_esc()
            
def mostrar_usuario(memoria):
    limpar_tela()
    print("Lista de todos os usuários cadastrados:")
    
    # Verifica se o dicionário está vazio
    if not memoria:
        print("Nenhum usuário cadastrado.")
    else:
        for (nome_usuario, senha_usuario) in memoria:
            print(f"Nome: {nome_usuario} - Senha: {senha_usuario}")
    
    voltar_esc()

    
def sair_s():
    
   while True:
        sair = verificacao.sair_do_sistema()
        
        if sair != 's' and sair != 'n':
            print("Entrada de dados invalida")
        elif sair == 's':
            sys.exit(0)
        elif sair == 'n':
            limpar_tela()
            return ReturnToMain()
        
        
