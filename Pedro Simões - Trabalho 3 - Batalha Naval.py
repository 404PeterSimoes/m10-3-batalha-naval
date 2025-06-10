# Batalha Naval - Pedro Simões

class Barco:
    def __init__(self, tamanho: int, orientacao: str, posicao_inicial: str, esta_afundado: bool):
        self.tamanho = tamanho
        self.orientacao = orientacao.upper()
        self.posicao_inicial = posicao_inicial.upper()
        self.coordenadas_ocupadas = self.calc_CoordenadasOcupadas()
        self.esta_afundado = esta_afundado

    def verificar_CoordenadasOcupadas(self):
        # Verificar se (coordenadas inseridas, tamanho do barco) é compatível com a área de jogo
        if tamanho == 5:

            if letra_inicial == ''







            

    def calc_CoordenadasOcupadas(self):
        
        letra_inicial = self.posicao_inicial[0]
        numero_inicial = int(self.posicao_inicial[1])

        # Adicionar as coordenadas do barco a uma lista de coordenadas
        coordenadas = []

        for i in range(self.tamanho):
            if self.orientacao == 'H':

                novo_numero = numero_inicial + i
                nova_coord = f'{letra_inicial}{novo_numero}'

            elif self.orientacao == 'V':
                nova_letra = chr(ord(letra_inicial) + i)
                nova_coord = f'{nova_letra}{numero_inicial}'
            
            coordenadas.append(nova_coord)

        return coordenadas

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

porta_aviao1 = Barco(tamanho, orientacao, posicao_inicial, False)

print(porta_aviao1.coordenadas_ocupadas)

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