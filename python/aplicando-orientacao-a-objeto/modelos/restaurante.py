class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Brasileira'
restaurante_praca.ativo = False

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria do João'
restaurante_pizza.categoria = 'Comida Italiana'
restaurante_pizza.ativo = False

print(restaurante_praca.nome)