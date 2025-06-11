# Batalha Naval - Pedro Simões

class Barco:
    def __init__(self, tamanho: int, orientacao: str, posicao_inicial: str):
        self.tamanho = tamanho
        self.orientacao = orientacao.upper()
        self.posicao_inicial = posicao_inicial.upper()

        if self.verificar_Coordenadas_tabuleiro():
            self.coordenadas_ocupadas = self.calc_CoordenadasOcupadas()

        

        self.esta_afundado = False

    def verificar_Coordenadas_tabuleiro(self) -> bool:
        # Verificar se (coordenadas inseridas, tamanho do barco) é compatível com a área de jogo

        letra_inicial = self.posicao_inicial[0]
        numero_inicial = int(self.posicao_inicial[1])


        if self.tamanho == 5:

            # Possibilidade ÁREA VERDE
            if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 70:
                if numero_inicial >= 0 and numero_inicial <= 5:
                    return True
            
            # Possibilidade (ÁREA AMARELA - baixo - horizontal)
            if self.orientacao == 'H':

                if ord(letra_inicial) >= 71 and ord(letra_inicial) <= 74:
                    if numero_inicial >= 0 and numero_inicial <= 5:
                        return True
                
            # Possibilidade (Área amarela - cima - vertical)
            if self.orientacao == 'V':

                if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 70:
                    if numero_inicial >= 6 and numero_inicial <= 9:
                        return True

            
            return False
        

        elif self.tamanho == 4:

            # Possibilidade ÁREA VERDE
            if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 71:
                if numero_inicial >= 0 and numero_inicial <= 6:
                    return True
            
            # Possibilidade (ÁREA AMARELA - baixo - horizontal)
            if self.orientacao == 'H':

                if ord(letra_inicial) >= 72 and ord(letra_inicial) <= 74:
                    if numero_inicial >= 0 and numero_inicial <= 6:
                        return True
                
            # Possibilidade (Área amarela - cima - vertical)
            if self.orientacao == 'V':

                if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 71:
                    if numero_inicial >= 7 and numero_inicial <= 9:
                        return True
                    

            return False
    

        elif self.tamanho == 3:

            # Possibilidade ÁREA VERDE
            if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 72:
                if numero_inicial >= 0 and numero_inicial <= 7:
                    return True
            
            # Possibilidade (ÁREA AMARELA - baixo - horizontal)
            if self.orientacao == 'H':

                if ord(letra_inicial) == 73 or ord(letra_inicial) == 74:
                    if numero_inicial >= 0 and numero_inicial <= 7:
                        return True
                
            # Possibilidade (Área amarela - cima - vertical)
            if self.orientacao == 'V':

                if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 72:
                    if numero_inicial == 8 or numero_inicial == 9:
                        return True
                    
                    
            return False
        
        
        elif self.tamanho == 2:

            # Possibilidade ÁREA VERDE
            if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 73:
                if numero_inicial >= 0 and numero_inicial <= 8:
                    return True
            
            # Possibilidade (ÁREA AMARELA - baixo - horizontal)
            if self.orientacao == 'H':

                if ord(letra_inicial) == 74:
                    if numero_inicial >= 0 and numero_inicial <= 8:
                        return True
                
            # Possibilidade (Área amarela - cima - vertical)
            if self.orientacao == 'V':

                if ord(letra_inicial) >= 65 and ord(letra_inicial) <= 73:
                    if numero_inicial == 9:
                        return True
                    
                    
            return False
  
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

    #def verificar_sobreposicao(self):

class Tabuleiro:
    def __init__(self):
        self.grelha = [['~' for _ in range(10)] for _ in range(10)]
        self.barcos = []

    def colocar_barco(self, barco: Barco):
        if barco.verificar_Coordenadas_tabuleiro(): # Se caso as coordenadas forem válidas no tabuleiro

            for coord in barco.coordenadas_ocupadas:
                letra_linha = ord(coord[0]) - 65
                num_coluna = int(coord[1])

                self.grelha[letra_linha][num_coluna] = 'B'
                self.barcos.append

    def mostrar_tabuleiro(self):
        print('  0 1 2 3 4 5 6 7 8 9')
        
        for i in range(10):
            linha_letra = chr(65 + i)
            linha_valores = ' '.join(self.grelha[i])

            print(f'{linha_letra} {linha_valores}')


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

tabuleiro_jogador = Tabuleiro()
tabuleiro_maquina = Tabuleiro()

print('\n/\ -- BATALHA NAVAL -- /\\\n')
nome = input('O meu NOME: ')

# jogador = Jogador(nome, tabuleiro1, barcos)

print('\n--- Inserir Barcos ---')

# ---------------------------------------------------

print('\nPorta-avião (5 células):\n')

orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))

porta_aviao1 = Barco(5, orientacao, posicao_inicial)

tabuleiro_jogador.colocar_barco(porta_aviao1)
tabuleiro_jogador.mostrar_tabuleiro()

# ---------------------------------------------------

print('\nCruzador (4 células):\n')

orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))

cruzador1 = Barco(4, orientacao, posicao_inicial)

tabuleiro_jogador.colocar_barco(cruzador1)
tabuleiro_jogador.mostrar_tabuleiro()

# ---------------------------------------------------

print('\nContratorpedeiro (3 células):\n')

orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))

contratorped1 = Barco(3, orientacao, posicao_inicial)

tabuleiro_jogador.colocar_barco(contratorped1)
tabuleiro_jogador.mostrar_tabuleiro()

# ---------------------------------------------------

print('\nContratorpedeiro (3 células:\n)')

orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))

contratorped2 = Barco(3, orientacao, posicao_inicial)

tabuleiro_jogador.colocar_barco(contratorped2)
tabuleiro_jogador.mostrar_tabuleiro()

# ---------------------------------------------------

print('\nSubmarino (2 células:\n)')

orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))

submarino1 = Barco(2, orientacao, posicao_inicial)

tabuleiro_jogador.colocar_barco(submarino1)
tabuleiro_jogador.mostrar_tabuleiro()

# ---------------------------------------------------

print('\nSubmarino (2 células:\n)')

orientacao = str(input('Introduz a orientação ( H / V ): '))
posicao_inicial = str(input('Introduz a posição inicial: '))

submarino2 = Barco(2, orientacao, posicao_inicial)

tabuleiro_jogador.colocar_barco(submarino2)
tabuleiro_jogador.mostrar_tabuleiro()



print(porta_aviao1.coordenadas_ocupadas)

# CONTINUAR AQUIIIIIIIIIIIIIIIIIIIII

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