# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# 3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# 4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# 5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro = Carro('Fusca', 'Azul', 1970)

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = 0
        self.comentarios = []

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante = Restaurante('Praça São Lourenço', 'Variado')
restaurante2 = Restaurante('Pizzaria', 'Pizza')
print(restaurante)
print(restaurante2)

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente = Cliente('João', 25, 'cliente_1@cliente.com.br', '11999999999')
cliente2 = Cliente('Maria', 30, 'cliente_2@cliente.com.br', '11999999999')
cliente3 = Cliente('Pedro', 35, 'cliente_3@cliente.com.br', '11999999999')

