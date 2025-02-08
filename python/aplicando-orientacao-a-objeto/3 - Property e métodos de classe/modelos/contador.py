class Contador:
    '''
    Classe que representa um contador.
    A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    '''

    contador_global = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f'Contador: {self.valor}'

    def incrementar(self):
        self.valor += 1

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        print('Contador global foi zerado.')
    

contador1 = Contador()
contador1.incrementar()
print(contador1)

Contador.zerar_contador_global()