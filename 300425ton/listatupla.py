

tarefas = {
    "urgente": [
        {"id": 1, "titulo": "Implementar autenticação de usuários", "responsavel": "João", "status": "pendente"},
        {"id": 2, "titulo": "Corrigir bug no carrinho de compras", "responsavel": "Maria", "status": "em andamento"}
    ],
    "prioritaria": [
        {"id": 3, "titulo": "Refatorar modelo de dados", "responsavel": "Carlos", "status": "concluida"},
        {"id": 4, "titulo": "Escrever testes unitários para API", "responsavel": "Ana", "status": "pendente"},
        {"id": 5, "titulo": "Reunião de planejamento da sprint", "responsavel": "Equipe de Desenvolvimento", "status": "agendada"}
    ],
    "normal": [
        {"id": 6, "titulo": "Atualizar documentação da API", "responsavel": "Pedro", "status": "pendente"},
        {"id": 7, "titulo": "Investigar lentidão em endpoint específico", "responsavel": "Lucas", "status": "em andamento"}
    ]
}

colaborador = {
    "id": 101,
    "nome": "Ana Silva",
    "cargo": "Engenheira de Software",
    "departamento": "Tecnologia"
}

def listar_tarefas(categoria="todas"):
    """Lista as tarefas por categoria (urgente, prioritaria, normal ou todas)."""
    print("\n--- Listagem de Tarefas ---")
    if categoria == "todas":
        for chave, lista_de_tarefas in tarefas.items():
            print(f"\nCategoria: {chave.capitalize()}")
            if lista_de_tarefas:
                for tarefa in lista_de_tarefas:
                    print(f"  ID: {tarefa['id']}, Título: {tarefa['titulo']}, Responsável: {tarefa['responsavel']}, Status: {tarefa['status']}")
            else:
                print("  Nenhuma tarefa nesta categoria.")
    elif categoria in tarefas:
        print(f"\nCategoria: {categoria.capitalize()}")
        if tarefas[categoria]:
            for tarefa in tarefas[categoria]:
                print(f"  ID: {tarefa['id']}, Título: {tarefa['titulo']}, Responsável: {tarefa['responsavel']}, Status: {tarefa['status']}")
        else:
            print("  Nenhuma tarefa nesta categoria.")
    else:
        print("Categoria inválida.")

def adicionar_tarefa(categoria, titulo, responsavel):
    """Adiciona uma nova tarefa à categoria especificada."""
    if categoria in tarefas:
        novo_id = max([tarefa['id'] for lista in tarefas.values() for tarefa in lista], default=0) + 1
        nova_tarefa = {"id": novo_id, "titulo": titulo, "responsavel": responsavel, "status": "pendente"}
        tarefas[categoria].append(nova_tarefa)
        print(f"\nTarefa '{titulo}' adicionada à categoria '{categoria.capitalize()}' com ID {novo_id}.")
    else:
        print("Categoria inválida.")

def alterar_status_tarefa(id_tarefa, novo_status):
    """Altera o status de uma tarefa com base no seu ID."""
    encontrada = False
    for categoria, lista_de_tarefas in tarefas.items():
        for tarefa in lista_de_tarefas:
            if tarefa['id'] == id_tarefa:
                tarefa['status'] = novo_status.lower()
                print(f"\nStatus da tarefa com ID {id_tarefa} alterado para '{novo_status}'.")
                encontrada = True
                break
        if encontrada:
            break
    if not encontrada:
        print(f"\nNenhuma tarefa encontrada com o ID {id_tarefa}.")

def remover_tarefa(id_tarefa):
    """Remove uma tarefa com base no seu ID."""
    encontrada = False
    for categoria, lista_de_tarefas in tarefas.items():
        for tarefa in list(lista_de_tarefas): # Iterar sobre uma cópia para permitir remoção
            if tarefa['id'] == id_tarefa:
                tarefas[categoria].remove(tarefa)
                print(f"\nTarefa com ID {id_tarefa} removida.")
                encontrada = True
                break
        if encontrada:
            break
    if not encontrada:
        print(f"\nNenhuma tarefa encontrada com o ID {id_tarefa}.")

def exibir_info_colaborador():
    """Exibe as informações do colaborador."""
    print("\n--- Informações do Colaborador ---")
    for chave, valor in colaborador.items():
        print(f"{chave.capitalize()}: {valor}")

def exibir_dicionario_compreensao():
    """Exibe o dicionário criado por compreensão."""
    dicionario_compreensao = {x: x**2 for x in range(5)}
    print("\n--- Dicionário por Compreensão ---")
    print(dicionario_compreensao)

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Menu de Opções ---")
    print("1 - Listar tarefas")
    print("2 - Listar tarefas por categoria")
    print("3 - Adicionar nova tarefa")
    print("4 - Alterar status de tarefa")
    print("5 - Remover tarefa")
    print("6 - Exibir informações do colaborador")
    print("7 - Exibir dicionário por compreensão")  # Nova opção
    print("0 - Sair")

def obter_opcao():
    """Obtém a opção escolhida pelo usuário."""
    return input("Digite o número da opção desejada: ")

def main():
    """Função principal para executar o sistema de gerenciamento de tarefas."""
    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == '1':
            listar_tarefas()
        elif opcao == '2':
            categoria = input("Digite a categoria desejada (urgente, prioritaria, normal): ").lower()
            listar_tarefas(categoria)
        elif opcao == '3':
            categoria = input("Digite a categoria da nova tarefa (urgente, prioritaria, normal): ").lower()
            titulo = input("Digite o título da nova tarefa: ")
            responsavel = input("Digite o responsável pela tarefa: ")
            adicionar_tarefa(categoria, titulo, responsavel)
        elif opcao == '4':
            try:
                id_tarefa = int(input("Digite o ID da tarefa que deseja alterar o status: "))
                novo_status = input("Digite o novo status da tarefa: ").lower()
                alterar_status_tarefa(id_tarefa, novo_status)
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == '5':
            try:
                id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))
                remover_tarefa(id_tarefa)
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == '6':
            exibir_info_colaborador()
        elif opcao == '7':  # Chama a função para exibir o dicionário por compreensão
            exibir_dicionario_compreensao()
        elif opcao == '0':
            print("\nSaindo do sistema. Até a próxima!")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()