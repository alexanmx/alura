# Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo

class Musica:
    nome = ''
    artista = ''
    duracao = int # em segundos

musica1 = Musica()
musica1.nome = 'Ainda bem'
musica1.artista = 'Marisa Monte'
musica1.duracao = 180

musica2 = Musica()
musica2.nome = 'Oceano'
musica2.artista = 'Djavan'
musica2.duracao = 240

musica3 = Musica()
musica3.nome = 'Faroeste Caboclo'
musica3.artista = 'Legião Urbana'
musica3.duracao = 600


musica4 = Musica()
musica4.nome = 'Bohemian Rhapsody'
musica4.duracao = 360

print(f'Música: {musica4.nome} - Banda: {musica4.artista} - {musica4.duracao} segundos')