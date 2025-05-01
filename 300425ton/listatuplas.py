import json

cadastro_funcionarios = {
    "funcionario_001": {
        "nome": "Ana",
        "idade": 25,
        "departamento": "RH",
        "salario": 3500.0,
        "ativo": True
    },
    "funcionario_002": {
        "nome": "João",
        "idade": 30,
        "departamento": "TI",
        "salario": 4800.0,
        "ativo": True
    },
    "funcionario_003": {
        "nome": "Clara",
        "idade": 28,
        "departamento": "Marketing",
        "salario": 4200.0,
        "ativo": False
    }
}

def adicionar_funcionario(codigo, nome, idade, departamento, salario, ativo=True):
    if codigo in cadastro_funcionarios:
        print("Erro: Funcionário já existe!")
    else:
        cadastro_funcionarios[codigo] = {
            "nome": nome,
            "idade": idade,
            "departamento": departamento,
            "salario": salario,
            "ativo": ativo
        }
        print(f"Funcionário {nome} adicionado com sucesso.")

def remover_funcionario(codigo):
    if codigo in cadastro_funcionarios:
        del cadastro_funcionarios[codigo]
        print(f"Funcionário {codigo} removido.")
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario(codigo, campo, novo_valor):
    if codigo in cadastro_funcionarios:
        if campo in cadastro_funcionarios[codigo]:
            cadastro_funcionarios[codigo][campo] = novo_valor
            print(f"{campo} atualizado com sucesso.")
        else:
            print("Campo inválido.")
    else:
        print("Funcionário não encontrado.")

def media_idade_ativos():
    ativos = [dados["idade"] for dados in cadastro_funcionarios.values() if dados["ativo"]]
    if ativos:
        media = sum(ativos) / len(ativos)
        print(f"Média de idade dos funcionários ativos: {media:.2f}")
    else:
        print("Nenhum funcionário ativo.")

def buscar_por_departamento(depto):
    encontrados = [v["nome"] for v in cadastro_funcionarios.values() if v["departamento"] == depto]
    if encontrados:
        print("Funcionários no departamento", depto + ":", encontrados)
    else:
        print("Nenhum funcionário nesse departamento.")

def exportar_para_json():
    with open("funcionarios.json", "w", encoding="utf-8") as f:
        json.dump(cadastro_funcionarios, f, ensure_ascii=False, indent=4)
    print("Dados exportados para 'funcionarios.json'.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar funcionário")
        print("2. Remover funcionário")
        print("3. Atualizar funcionário")
        print("4. Média de idade dos ativos")
        print("5. Buscar por departamento")
        print("6. Exportar dados para JSON")
        print("7. Mostrar todos")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cod = input("Código: ")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            depto = input("Departamento: ")
            salario = float(input("Salário: "))
            adicionar_funcionario(cod, nome, idade, depto, salario)
        elif escolha == "2":
            cod = input("Código do funcionário a remover: ")
            remover_funcionario(cod)
        elif escolha == "3":
            cod = input("Código: ")
            campo = input("Campo a atualizar (nome, idade, departamento, salario, ativo): ")
            if campo == "idade":
                valor = int(input("Novo valor: "))
            elif campo == "salario":
                valor = float(input("Novo valor: "))
            elif campo == "ativo":
                valor = input("Ativo? (True/False): ") == "True"
            else:
                valor = input("Novo valor: ")
            atualizar_funcionario(cod, campo, valor)
        elif escolha == "4":
            media_idade_ativos()
        elif escolha == "5":
            depto = input("Departamento: ")
            buscar_por_departamento(depto)
        elif escolha == "6":
            exportar_para_json()
        elif escolha == "7":
            print(json.dumps(cadastro_funcionarios, indent=4, ensure_ascii=False))
        elif escolha == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

menu()

    
