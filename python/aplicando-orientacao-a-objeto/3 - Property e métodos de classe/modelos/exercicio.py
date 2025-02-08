# 1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# 2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# 3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# 4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# 5. Crie uma instância da classe e imprima o valor da propriedade titular.

# 6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# 7. Crie um método de classe para a conta ClienteBanco.

class Conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'Conta de {self.titular} com saldo de R${self.saldo:.2f}'

    def ativar_conta(self):
        self.ativo = True
    

conta_1 = Conta_bancaria('Alice', 1000)
print(conta_1)

conta_2 = Conta_bancaria('Luiza', 2000)
print(conta_2)

conta_1.ativar_conta()
print(conta_1.ativo)

