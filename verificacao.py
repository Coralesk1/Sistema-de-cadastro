from datetime import datetime
import re
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def nome_v():
    while True:
        print("📄 " + "=" * 20 + " Cadastro de Nome " + "=" * 20 + " 📄")
        nome = str(input("Nome completo: ")).strip()
        erros = []
 
        if len(nome) < 3 or len(nome) > 50:
            erros.append("Seu nome deve ter entre 3 e 50 caracteres.")
        if not nome.replace(" ", "").isalpha():
            erros.append("O nome deve conter apenas letras.")
        if " " not in nome:
            erros.append("Por favor, forneça um nome completo.")
        if erros:
            print("⚠️  Erros encontrados:")
            for erro in erros:
                print(f"- {erro}")
        else:
            return nome

def senha_v():
    while True:
        print("🔒 " + "=" * 20 + " Configuração de Senha " + "=" * 20 + " 🔒")
        senha = input("Digite sua senha: ")
        
        if (len(senha) < 8 or
            not re.search(r"[A-Z]", senha) or  
            not re.search(r"[a-z]", senha) or  
            not re.search(r"[0-9]", senha) or
            re.search(r" ") or 
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha)):
            
            print("⚠️ Senha inválida. A senha deve ter pelo menos 8 caracteres e incluir uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")
        else:
            print("✅ Senha válida.")
        return senha  

def idade_v():
    while True:
        print("🎂 " + "=" * 20 + " Validação de Idade " + "=" * 20 + " 🎂")
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0 or idade > 120:
                print("⚠️ Por favor, insira uma idade entre 0 e 120.")
            else:
                return idade
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, insira um número inteiro.")

def cidade_v():
    while True:
        print("🏙️ " + "=" * 20 + " Cadastro de Cidade " + "=" * 20 + " 🏙️")
        cidade = input("Digite o nome da cidade: ").strip()
        
        if all(char.isalpha() or char.isspace() for char in cidade):
            return cidade
        else:
            print("⚠️ Entrada inválida. A cidade deve conter apenas letras e espaços.")

def validar_cep():
    while True:
        print("📮 " + "=" * 20 + " Validação de CEP " + "=" * 20 + " 📮")
        cep = input("Digite o CEP (formato XXXXX-XXX): ").strip()
        
        cep = cep.replace(" ", "")

        if re.match(r'^\d{5}-\d{3}$', cep):
            return cep
        else:
            print("⚠️ CEP inválido. Certifique-se de que está no formato correto (XXXXX-XXX).")

def validar_data_nascimento():
    while True:
        print("📅 " + "=" * 20 + " Data de Nascimento " + "=" * 20 + " 📅")
        data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
            data_atual = datetime.now()
            
            idade = data_atual.year - data_nascimento.year - (
                (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day)
            )

            if 0 < idade < 120:
                return data_nascimento.strftime("%d/%m/%Y")
            else:
                print("⚠️ Data inválida. Insira uma data de nascimento que resulte em uma idade entre 0 e 120 anos.")

        except ValueError:
            print("⚠️ Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")

def rua_v():
    while True:
        print("🚏 " + "=" * 20 + " Cadastro de Rua " + "=" * 20 + " 🚏")
        rua = input("Digite o nome da rua: ").strip()
        if rua.replace(" ", "").isalnum() and len(rua) >= 3:
            return rua
        print("⚠️ Nome de rua inválido. Use apenas letras e números, e insira ao menos 3 caracteres.")

def cpf_v():
    while True:
        print("📜 " + "=" * 20 + " Validação de CPF " + "=" * 20 + " 📜")
        entrada_do_cpf = input("CPF no formato(XXX.XXX.XXX-XX): ").strip()
        cpf = re.sub(r'[^0-9]', '', entrada_do_cpf)

        entrada_eh_sequencial = entrada_do_cpf == entrada_do_cpf[0] * len(entrada_do_cpf)

        if entrada_eh_sequencial:
            print("⚠️ Você enviou dados sequenciais.")
        
        nove_digitos = cpf[:9]
        contador_regressivo = 10
        resultado = 0

        for digito in nove_digitos:
            resultado += int(digito) * contador_regressivo
            contador_regressivo -= 1
        resto_divisao = (resultado * 10) % 11
        condição = resto_divisao >= 9
        verificao_digito_final = 0 if condição else f"O primeiro dígito do CPF é {resto_divisao}"

        cpffinal = f'{nove_digitos}{verificao_digito_final}'
        dez_digitos = cpf[:10]
        contador_regressivo_2 = 11
        resultado_2 = 0

        for digito in dez_digitos:
            resultado_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        resto_divisao_2 = (resultado_2 * 10) % 11
        condição_2 = resto_divisao_2 >= 9
        verificao_digito_final_2 = 0 if condição_2 else resto_divisao_2
        cpffinal = f"{dez_digitos}{verificao_digito_final_2}"

        if cpffinal == cpf:
            print(f"✅ Esse CPF {cpf} é válido.")
            return cpf
        else: 
            print("⚠️ CPF inválido.")

def nome_dados():
    while True:
        nome_usuario = str(input("Nome completo: ")).strip()
        erros = []
 
        if len(nome_usuario) < 3 or len(nome_usuario) > 50:
            erros.append("Seu nome deve ter entre 3 e 50 caracteres.")
        if not nome_usuario.replace(" ", "").isalpha():
            erros.append("O nome deve conter apenas letras.")
        if " " not in nome_usuario:
            erros.append("Por favor, forneça um nome completo.")
        if erros:
            print("Erros encontrados:")
            for erro in erros:
                print(f"- {erro}")
        else:
            return nome_usuario
        
def senha_dados():
    while True:
        senha_usuario = input("Digite sua senha (mínimo de 8 caracteres, pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial): ").strip()
        return senha_usuario

def sair_do_sistema():
    print("🚪 " + "=" * 20 + " Sair do Sistema " + "=" * 20 + " 🚪")
    sair = input("Você deseja sair [S/N]? ").strip().lower()
    return sair
