import datetime

class Conta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${-valor:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            return True
        else:
            print("Saldo insuficiente ou valor inválido para saque.")
            return False

    def transferir(self, valor, conta_destino):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            conta_destino.depositar(valor)
            self.extrato.append(f"Transferência enviada: R${-valor:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            conta_destino.extrato.append(f"Transferência recebida: R${valor:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            return True
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")
            return False

    def exibir_extrato(self):
        print(f"\n--- Extrato da Conta {self.titular} ---")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        for operacao in self.extrato:
            print(operacao)
        print(f"--------------------------------------------------")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"--------------------------------------------------")