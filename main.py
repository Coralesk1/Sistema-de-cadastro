from defs import cadastro, dados_usuario, sair_s, mostrar_usuario, ReturnToMain
import os


memoria = {}

def limpar_tela():
    os.system('cls')

def limpar_tela():
    print("\n" * 100)  # Limpa a tela no terminal, simulando uma nova página

def menu_principal():
    while True:
        limpar_tela()
        print("=" * 40)
        print(" " * 10 + "📋 MENU DE OPÇÕES 📋")
        print("=" * 40)
        print("1 - Cadastro")
        print("2 - Dados do Usuário")
        print("3 - Mostrar Clientes")
        print("0 - Sair")
        print("=" * 40)
        
        opcoes = input("🔹 Insira a opção desejada: ")
        
        # Verifica se a opção é válida
        if opcoes not in ['1', '2', '3', '0']:
            limpar_tela()
            print("⚠️ Opção inválida. Tente novamente.")
            continue
        
        try:
            # Executa a ação correspondente à opção escolhida
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
                print("🛑 Saindo do sistema... Obrigado!")
                break  # Encerra o loop para sair do menu
        except ReturnToMain:
            print("↩️ Retornando ao menu principal.")
            input("Pressione Enter para continuar...")

# Chama o menu principal
menu_principal()










