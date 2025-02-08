class Musica:
    artistas = []

    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.artistas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    def listar_artistas():
        for artista in Musica.artistas:
            print(f'{artista.nome} | {artista.artista} | {artista.duracao}')

musica_1 = Musica('Astronaut in the Ocean', 'Masked Wolf', 2.46)
musica_2 = Musica('Save Your Tears', 'The Weeknd', 3.35)

Musica.listar_artistas()