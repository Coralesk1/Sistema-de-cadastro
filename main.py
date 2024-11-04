from defs import cadastro, dados_usuario, sair_s, mostrar_usuario, ReturnToMain
import os

memoria = {}

def limpar_tela():
    os.system('cls')
    

def menu_principal():
    while True:
        print("=" * 40)
        print(" " * 10 + "📋 MENU DE OPÇÕES 📋")
        print("=" * 40)
        print("1 - Cadastro")
        print("2 - Dados do Usuário")
        print("3 - Mostrar Clientes")
        print("0 - Sair")
        print("=" * 40)
        
        opcoes = input("🔹 Insira a opção desejada: ")
        
        if opcoes not in ['1', '2', '3', '0']:
            print("⚠️ Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
            continue

        try:
            if opcoes == '1':
                limpar_tela()
                cadastro(memoria)  
            elif opcoes == '2':
                limpar_tela()
                dados_usuario(memoria)
            elif opcoes == '3':
                limpar_tela()
                mostrar_usuario(memoria)
            elif opcoes == '0':
                sair_s()
                
        except ReturnToMain:
            print("↩️ Retornando ao menu principal.")
            limpar_tela()

menu_principal()









