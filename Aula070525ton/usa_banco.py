from banco import Conta
import datetime

def exibir_menu():
    print("\n--- Menu Bancário ---")
    print("1. Ver Saldo")
    print("2. Adicionar Saldo")
    print("3. Fazer Transferência")
    print("4. Ver Extrato")
    print("5. Adicionar Conta")
    print("6. Sair")
    print("---------------------")

def obter_numero_conta(mensagem="Digite o número da conta: "):
    return input(mensagem).strip().upper()

def obter_nome_titular(mensagem="Digite o nome do titular da conta: "):
    return input(mensagem).strip()

def obter_valor(mensagem="Digite o valor: "):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número.")

def main():
    contas = {
        "E36EB738": Conta("Mariana Costa", 500.00),
        "A81669A2": Conta("Gustavo Lima", 1000.00)
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            numero_conta = obter_numero_conta()
            if numero_conta in contas:
                print(f"Saldo da conta {numero_conta}: R${contas[numero_conta].saldo:.2f}")
            else:
                print("Conta não encontrada.")
        elif opcao == '2':
            numero_conta = obter_numero_conta("Digite o número da conta para adicionar saldo: ")
            if numero_conta in contas:
                valor = obter_valor("Digite o valor a ser adicionado: ")
                contas[numero_conta].depositar(valor)
                print("Depósito realizado com sucesso.")
            else:
                print("Conta não encontrada.")
        elif opcao == '3':
            conta_origem = obter_numero_conta("Digite o número da conta de origem: ")
            if conta_origem not in contas:
                print("Conta de origem não encontrada.")
                continue
            conta_destino = obter_numero_conta("Digite o número da conta de destino: ")
            if conta_destino not in contas:
                print("Conta de destino não encontrada.")
                continue
            valor = obter_valor("Digite o valor a ser transferido: ")
            if contas[conta_origem].transferir(valor, contas[conta_destino]):
                print("Transferência realizada com sucesso.")
            else:
                print("Saldo insuficiente.")
        elif opcao == '4':
            numero_conta = obter_numero_conta()
            if numero_conta in contas:
                contas[numero_conta].exibir_extrato()
            else:
                print("Conta não encontrada.")
        elif opcao == '5':
            print("\n--- Adicionar Nova Conta ---")
            novo_numero_conta = obter_numero_conta("Digite o número da nova conta: ")
            if novo_numero_conta in contas:
                print("Número de conta já existente.")
            else:
                nome_titular = obter_nome_titular("Digite o nome do titular: ")
                saldo_inicial = obter_valor("Digite o saldo inicial (opcional, digite 0 se não houver): ")
                contas[novo_numero_conta] = Conta(nome_titular, saldo_inicial)
                print(f"Conta {novo_numero_conta} criada para {nome_titular} com saldo inicial de R${saldo_inicial:.2f}.")
        elif opcao == '6':
            print("Saindo do sistema bancário.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção do menu.")

if __name__ == "__main__":
    main()