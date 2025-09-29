import time


class ContaBancária:
    def __init__(self, titular):
        self.saldo = 0
        self.titular = titular

    def depositar(self, valor):
        self.valor = valor
        self.saldo += valor
        print(f"A quantia de {valor} foi depositada na conta do usuário {self.titular}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"O valor de {valor} foi retirado com sucesso da conta do usuário {self.titular}")
        else:
            print(f"Você não tem saldo o suficiente, precisa de {valor}, mas você só tem {self.saldo}")

conta_joao = ContaBancária("João Silva")
conta_joao.depositar(500)
print(conta_joao.saldo)

conta_maria = ContaBancária("Maria Souza")
conta_maria.depositar(1000)
conta_maria.sacar(300)
time.sleep(1)  # Deve ter sucesso e mostrar 700
conta_maria.sacar(900)   # Deve falhar e mostrar "Saldo insuficiente"


class ContaPoupanca(ContaBancária):
    def render_juros(self, taxa_juros):
        juros = taxa_juros * self.saldo
        self.saldo += juros
        print(f"Juros adicionado ao rendimento da conta {self.titular}, novo saldo de: {self.saldo}")

conta_filha_maria = ContaPoupanca("Mariazinha")
conta_filha_maria.depositar(100)
time.sleep(1)
conta_filha_maria.sacar(99)
time.sleep(1)
conta_filha_maria.sacar(2)
conta_filha_maria.render_juros(0.1)
        


