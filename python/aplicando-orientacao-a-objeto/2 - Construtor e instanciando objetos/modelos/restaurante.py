class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_resturantes():
        for resturante in Restaurante.restaurantes:
            print(f'{resturante.nome} | {resturante.categoria} | {resturante.ativo}')

# # agora tenho que passar nome e categoria para o construtor
# # senão vai dar erro
# restaurante_praca = Restaurante()
# print(restaurante_praca)

# restaurante_praca = Restaurante('Praça São Lourenço', 'Variado')
# print(restaurante_praca)

# # exibir todos os métodos e atributos de um objeto
# print(dir(restaurante_praca))

# # exibir o objeto em formato de texto
# print(restaurante_praca)

# métodos
restaurante_praca = Restaurante('Praça São Lourenço', 'Variado')
restaurante_rua = Restaurante('Pizzaria', 'Pizza')

Restaurante.listar_resturantes()