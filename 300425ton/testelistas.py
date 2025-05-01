def criar_novo_usuario(cadastro):
    """Cria um novo usuário bancário e adiciona ao sistema de cadastro."""
    novo_cliente = {}
    novo_cliente['nome_completo'] = input("Digite seu nome completo: ")
    novo_cliente['cpf'] = input("Digite seu CPF (apenas números): ")
    # Em uma aplicação real, você teria validação de CPF
    novo_cliente['data_nascimento'] = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    # Em uma aplicação real, você teria validação de data
    novo_cliente['endereco'] = input("Digite seu endereço completo: ")
    novo_cliente['telefone'] = input("Digite seu telefone com DDD (apenas números): ")
    # Em uma aplicação real, você teria validação de telefone
    novo_cliente['email'] = input("Digite seu e-mail: ")
    # Em uma aplicação real, você teria validação de e-mail
    novo_cliente['login'] = input("Escolha um nome de usuário (login): ")
    # Em uma aplicação real, você verificaria se o login já existe
    senha = input("Crie uma senha: ")
    confirmacao_senha = input("Confirme sua senha: ")
    while senha != confirmacao_senha:
        print("As senhas não coincidem. Tente novamente.")
        senha = input("Crie uma senha: ")
        confirmacao_senha = input("Confirme sua senha: ")
    # Em uma aplicação real, você HASHEARIA a senha antes de armazenar
    novo_cliente['senha'] = senha
    novo_cliente['saldo'] = 0.0  # Saldo inicial

    cadastro.append(novo_cliente)
    print(f"\nCadastro de {novo_cliente['nome_completo']} realizado com sucesso!")

def exibir_usuarios(cadastro):
    """Exibe a lista de usuários cadastrados (apenas para demonstração)."""
    if not cadastro:
        print("Nenhum usuário cadastrado ainda.")
        return
    print("\n--- Usuários Cadastrados ---")
    for i, cliente in enumerate(cadastro):
        print(f"ID: {i+1}")
        print(f"  Nome: {cliente['nome_completo']}")
        print(f"  Login: {cliente['login']}")
        print("---------------------------")

cadastro_usuarios = []

while True:
    print("\n--- Menu de Cadastro ---")
    print("1. Criar Novo Usuário")
    print("2. Exibir Usuários Cadastrados")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        criar_novo_usuario(cadastro_usuarios)
    elif opcao == '2':
        exibir_usuarios(cadastro_usuarios)
    elif opcao == '3':
        print("Saindo do sistema de cadastro.")
        break
    else:
        print("Opção inválida. Tente novamente.")