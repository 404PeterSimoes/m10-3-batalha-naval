# Batalha Naval - Pedro Simões

class Barco:
    def _init_(self, tamanho, orientacao, posicao_inicial, coordenada_ocupadas,
               esta_afundado):
        self.tamanho = tamanho
        self.orientacao = orientacao
        self.posicao_inicial = posicao_inicial
        self.coordenadas_ocupadas = coordenada_ocupadas
        self.esta_afundado = esta_afundado

# class Tabuleiro:
    # def colocar_barco(Barco):

    # def receber_tiro(coord):

    # def mostrar(): (mostrar o tabuleiro)

# Pode ser o jogador ou o computador
class Jogador:
    def __init__(self, nome, o_seu_tabuleiro, lista_barcos):
        self.nome = nome
        self.o_seu_tabuleiro = o_seu_tabuleiro
        self.lista_barcos = lista_barcos

    # def efetuar_tiro(): 

"""
print('  0 1 2 3 4 5 6 7 8 9\n'
      'A ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'B ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'C ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'D ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'E ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'F ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'G ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'H ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'I ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
      'J ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
"""

# INÍCIO AQUI

print('\n/\ -- BATALHA NAVAL -- /\\\n')



x = [
    [1, 2, 3],
    [4, 5, 6]
]

print(x[0][2])