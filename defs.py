import os
import verificacao
import sys

class ReturnToMain(Exception):
    pass

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def voltar_esc():
    input("Pressione Enter para continuar...")
    raise ReturnToMain()
    
def cadastro(memoria):
    while True:
        limpar_tela()
        nome = verificacao.nome_v()
        senha = verificacao.senha_v()
        idade = verificacao.idade_v()
        data_nascimento = verificacao.validar_data_nascimento()
        cpf = verificacao.cpf_v()
        cidade = verificacao.cidade_v()
        rua = verificacao.rua_v()
        cep = verificacao.validar_cep()
        
        memoria[(nome, senha)] = {
            "idade": idade,
            "data": data_nascimento,
            "cpf": cpf,
            "cidade": cidade,
            "rua": rua,
            "cep": cep
        }

        continuar = input("Deseja adicionar outra pessoa? (S/N): ").lower()
        if continuar == 'n':
            limpar_tela()
            print("Dados cadastrados.")
            raise ReturnToMain()
        
def dados_usuario(memoria):
    while True:
        limpar_tela()
        print("🔍 Buscando dados do usuário...")

        nome_usuario = verificacao.nome_dados()
        senha_usuario = verificacao.senha_dados()
       
        if (nome_usuario, senha_usuario) in memoria:
            limpar_tela()
            dados = memoria[(nome_usuario, senha_usuario)]
            print(f"Nome: {nome_usuario}")
            print(f"Senha: {senha_usuario}")
            print(f"Idade: {dados['idade']}")
            print(f"Data: {dados['data']}")
            print(f"CPF: {dados['cpf']}")
            print(f"Cidade: {dados['cidade']}")
            print(f"Rua: {dados['rua']}")
            print(f"Cep: {dados['cep']}")
            input("Pressione Enter para voltar...")
            limpar_tela()
            return
        else:
            print("Usuário não encontrado.")
        voltar_esc()

def mostrar_usuario(memoria):
    limpar_tela()
    print("Lista de todos os usuários cadastrados:")
    
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
            limpar_tela()
            print("🛑 Saindo do sistema... Obrigado!")
            sys.exit(0)
        elif sair == 'n':
            limpar_tela()
            return ReturnToMain()
