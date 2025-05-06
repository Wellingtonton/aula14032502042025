import csv
import os

NOME_ARQUIVO = "usuarios.csv"

def adicionar_usuario(nome, email):
    """Adiciona um novo usuário ao arquivo."""
    with open(NOME_ARQUIVO, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        # Se o arquivo estiver vazio, escreve o cabeçalho
        if os.stat(NOME_ARQUIVO).st_size == 0:
            escritor.writerow(['Nome', 'Email'])
        escritor.writerow([nome, email])
    print(f"Usuário '{nome}' adicionado com sucesso.")

def listar_usuarios():
    """Lista todos os usuários armazenados no arquivo (usando csv.reader)."""
    usuarios = []
    if os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor, None)  # Pula o cabeçalho, se existir
            for linha in leitor:
                if linha:  # Garante que a linha não está vazia
                    usuarios.append({'Nome': linha[0], 'Email': linha[1]})
    if usuarios:
        print("\nLista de Usuários (usando csv.reader):")
        for usuario in usuarios:
            print(f"- Nome: {usuario['Nome']}, Email: {usuario['Email']}")
    else:
        print("\nNenhum usuário cadastrado.")

def listar_usuarios_com_readlines():
    """Lista todos os usuários armazenados no arquivo (usando readlines())."""
    usuarios = []
    if os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            if linhas and len(linhas) > 1:  # Garante que há dados além do cabeçalho
                cabecalho = linhas[0].strip().split(',')
                for linha in linhas[1:]:
                    linha_dados = linha.strip().split(',')
                    if len(linha_dados) == 2:
                        usuarios.append({'Nome': linha_dados[0], 'Email': linha_dados[1]})
            if usuarios:
                print("\nLista de Usuários (usando readlines()):")
                for usuario in usuarios:
                    print(f"- Nome: {usuario['Nome']}, Email: {usuario['Email']}")
            else:
                print("\nNenhum usuário cadastrado.")
    else:
        print("\nNenhum usuário cadastrado.")

def excluir_usuario(nome_para_excluir):
    """Exclui um usuário do arquivo pelo nome."""
    usuarios_mantidos = []
    usuario_excluido = False
    if os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'r', newline='', encoding='utf-8') as arquivo_leitura:
            leitor = csv.reader(arquivo_leitura)
            cabecalho = next(leitor, None)
            for linha in leitor:
                if linha and linha[0] != nome_para_excluir:
                    usuarios_mantidos.append(linha)
                elif linha and linha[0] == nome_para_excluir:
                    usuario_excluido = True

        with open(NOME_ARQUIVO, 'w', newline='', encoding='utf-8') as arquivo_escrita:
            escritor = csv.writer(arquivo_escrita)
            if cabecalho:
                escritor.writerow(cabecalho)
            escritor.writerows(usuarios_mantidos)

        if usuario_excluido:
            print(f"Usuário '{nome_para_excluir}' excluído com sucesso.")
        else:
            print(f"Usuário '{nome_para_excluir}' não encontrado.")
    else:
        print("Nenhum usuário cadastrado ainda.")

def main():
    while True:
        print("\nOpções:")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários (usando csv.reader)")
        print("3. Listar Usuários (usando readlines())")
        print("4. Excluir Usuário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            adicionar_usuario(nome, email)
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            listar_usuarios_com_readlines()
        elif opcao == '4':
            nome_para_excluir = input("Digite o nome do usuário que deseja excluir: ")
            excluir_usuario(nome_para_excluir)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()