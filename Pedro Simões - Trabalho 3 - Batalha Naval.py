# Batalha Naval - Pedro Simões

class Barco:
    def _init_(self, tamanho: int, orientacao: str, posicao_inicial: str,
               coordenada_ocupadas: list, esta_afundado: bool):
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
    def __init__(self, nome: str, o_seu_tabuleiro, lista_barcos: list):
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
"""
tabuleiro_jogador = [
    ['null', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['A', 'A0' 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
    ['B', 'B0' 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
    ['C', 'C0' 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
    ['D', 'D0' 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
    ['E', 'E0' 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9']
    ['F', 'F0' 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9']
    ['G', 'G0' 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']
    ['H', 'H0' 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9']
    ['I', 'I0' 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
    ['J', 'J0' 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9']
]
"""

# INÍCIO AQUI

print('\n/\ -- BATALHA NAVAL -- /\\\n')
nome = input('O meu NOME: ')

print('\n--- Inserir Barcos ---')

print('\nPorta-avião (5 células):\n')
tamanho = 5
orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))
# coordenadas_ocupadas (vou fazer uma funcao para calcular)
esta_afundado = False

porta_aviao1 = Barco("colocar aqui as coisas")

# cruzador1

# contratorped1

# contratorped2

# submarino1

# submarino2

x = [
    [1, 2, 3],
    [4, 5, 6]
]

#print(x[0][2])