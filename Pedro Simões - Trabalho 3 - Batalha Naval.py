# Batalha Naval - Pedro Simões

import os
import random
from time import sleep

class Barco:
    def __init__(self, tamanho: int, orientacao: str, posicao_inicial: str):
        self.tamanho = tamanho
        self.orientacao = orientacao.upper()
        self.posicao_inicial = posicao_inicial.upper()
        self.coordenadas_ocupadas = self.calc_CoordenadasOcupadas()
        self.posicoes_atingidas = []

    # Verificar se (coordenadas inseridas, tamanho do barco) é compatível com a área de jogo
    def verificar_Coordenadas_tabuleiro(self) -> bool:

        if (len(self.posicao_inicial) != 2 or ord(self.posicao_inicial[0]) < 65
            or ord(self.posicao_inicial[0]) > 74 or not self.posicao_inicial[1].isdigit()):

            return False

        letra_inicial = ord(self.posicao_inicial[0])
        num_inicial = int(self.posicao_inicial[1])

        if self.orientacao == 'H':

            if letra_inicial >= 65 and letra_inicial <= 74:
                if num_inicial >= 0 and num_inicial <= 10 - (self.tamanho):
                    return True
                    
            return False

        if self.orientacao == 'V':

            if letra_inicial >= 65 and (letra_inicial - 65) <= (10 - self.tamanho):
                if num_inicial >= 0 and num_inicial <= 9:
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

    # Verificar se o barco está completamente afundado
    def verificar_esta_afundado(self) -> bool:
        return len(self.posicoes_atingidas) == self.tamanho

    def receber_tiro(self, coord: str) -> bool:

        # Verificar se a coordenada introduzida estiver a ser ocupada por um barco
        if coord in self.coordenadas_ocupadas:

            # Verificar se a coordenada não foi atingida
            if coord not in self.posicoes_atingidas:
                self.posicoes_atingidas.append(coord)
            
            return True
        
        return False


class Tabuleiro:
    def __init__(self):
        self.grelha = [['~' for _ in range(10)] for _ in range(10)]
        self.barcos = []
        self.tiros_recebidos = []

    def colocar_barco(self, barco: Barco):
        if barco.verificar_Coordenadas_tabuleiro(): # Se caso as coordenadas forem válidas no tabuleiro

        # Verificar sobreposição com barcos existentes
            for outro_barco in self.barcos:

                for coord in barco.coordenadas_ocupadas:
                    if coord in outro_barco.coordenadas_ocupadas:

                        return False

            # Se não houver sobreposição, o barco será colocado
            for coord in barco.coordenadas_ocupadas:
                letra_linha = ord(coord[0]) - 65
                num_coluna = int(coord[1])

                self.grelha[letra_linha][num_coluna] = 'B'
            
            self.barcos.append(barco)
            return True
        
        else:
            return False
 
    def receber_tiro(self, coord: str):

        # Verificar se a coordenada recebida já foi atacada
        if coord in self.tiros_recebidos:
            return 'ja_atacado' # Pode se colocar no futuro verdadeiro ou falso
        
        self.tiros_recebidos.append(coord)

        # Verificar se acertou algum barco
        for barco in self.barcos:
            if barco.receber_tiro(coord):

                letra_linha = ord(coord[0]) - 65
                num_coluna = int(coord[1])
                self.grelha[letra_linha][num_coluna] = 'X'

                if barco.verificar_esta_afundado():
                    return 'afundado'
                else:
                    return 'acertou'
                
        # Se não acertou nenhum barco
        letra_linha = ord(coord[0]) - 65
        num_coluna = int(coord[1])

        self.grelha[letra_linha][num_coluna] = 'O'
        return 'falhou'

    def mostrar_tabuleiro(self, visivel = True):
        print('\n  0 1 2 3 4 5 6 7 8 9')
        
        # Letras = primeiríssima coluna (A, B, C, ...)
        # Linha_valores = (~, B, X, O) 

        for i in range(10): # Escrever todos os valores eixo vertical - linhas
            letra = chr(65 + i)
            linha_valores = []

            for j in range(10): # Escrever todos os valores eixo horizontal - colunas
                atual = self.grelha[i][j]

                if not visivel and atual == 'B':
                    linha_valores.append('~')
                else:
                    linha_valores.append(atual)

            print(f'{letra} {' '.join(linha_valores)}')

    # Verificar se todos os barcos estão afundados    
    def todos_barcos_afundados(self) -> bool:

        for barco in self.barcos:
            if barco.verificar_esta_afundado() == False:
                return False
        
        return True


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.tabuleiro = Tabuleiro()
        self.lista_barcos = []
        self.pontos = 0

    def efetuar_tiro(self, tabuleiro_adversario: Tabuleiro):

        escrever_entrada = True

        # Ciclo "infinito"
        while True:

            if escrever_entrada == True:
                coord = input(f'\n{self.nome}, introduz uma coordenada para disparar: ').upper()

            #Validar o formato da coordenada
            if len(coord) != 2 or ord(coord[0]) < 65 or ord(coord[0]) > 74 or not coord[1].isdigit():
                escrever_entrada = False
                coord = input('\nCoordenada inválida.\nTenta novamente, introduz uma coordenada'
                                ' para disparar: ').upper()
                continue

            sleep(1)
            resultado = tabuleiro_adversario.receber_tiro(coord)

            if resultado == 'ja_atacado':
                escrever_entrada = False
                coord = input('\n❌ Já atacaste essa posição!\nTenta novamente, introduz uma'
                              ' coordenada para disparar: ')
                continue

            elif resultado == 'acertou':
                print('\n🎯 Parabéns, ACERTASTE um barco!\n')
                
            elif resultado == 'afundado':
                print('\n💥 Parabéns, ACERTASTE e AFUNDASTE um barco!\n')

            elif resultado == 'falhou':
                print('\nFalhaste!')

            return resultado

class Computador(Jogador):
    def __init__(self):
        super().__init__('Computador')
        self.posicoes_atacadas = []

    def posicionar_barcos_random(self):
        tipos_barcos = [5, 4, 3, 3, 2, 2]

        for tamanho in tipos_barcos:
            colocado = False

            while not colocado:
                orientacao = random.choice(['H', 'V'])

                if orientacao == 'H':
                    letra_linha = random.randint(0, 9)
                    num_coluna = random.randint(0, 10 - tamanho)
                else:
                    letra_linha = random.randint(0, 10 - tamanho)
                    num_coluna = random.randint(0, 9)

                posicao_inicial = f'{chr(65 + letra_linha)}{num_coluna}'
                
                barco = Barco(tamanho, orientacao, posicao_inicial)

                if self.tabuleiro.colocar_barco(barco):
                    self.lista_barcos.append(barco)
                    colocado = True

    # Método para o computador efetuar um tiro (aleatório)
    def efetuar_tiro(self, tabuleiro_adversario: Tabuleiro):
        
        while True:
            letra_linha = random.randint(0, 9)
            num_coluna = random.randint(0, 9)
            coord = f'{chr(65 + letra_linha)}{num_coluna}'

            if coord not in self.posicoes_atacadas:
                self.posicoes_atacadas.append(coord)

                resultado = tabuleiro_adversario.receber_tiro(coord)

                sleep(1)

                if resultado == 'acertou':
                    print(f'O computador disparou em {coord} e\n'
                           '🎯 ACERTOU um dos teus barcos!\n\n'
                           'Ele tem direito a mais uma jogada.\n')

                elif resultado == "afundado":
                    print(f'O computador disparou em {coord} e\n'
                          '💥 ACERTOU e AFUNDOU um dos teus barcos!\n\n'
                          'Ele tem direito a mais uma jogada.\n')
                    
                elif resultado == 'falhou':
                    print(f'O computador disparou em {coord} e\nFALHOU!\n')

                return resultado
                

def inserir_barcos_jogador(jogador: Jogador):

    print('\nIntroduz os barcos no teu TABULEIRO:')

    tipos_barcos = [
        (5, 'Porta-avião'),
        (4, 'Cruzador'),
        (3, 'Contratorpedeiro'),
        (3, 'Contratorpedeiro'),
        (2, 'Submarino'),
        (2, 'Submarino')
    ]

    for tamanho, tipo in tipos_barcos:

        verificacao = False
        
        while not verificacao:
            jogador.tabuleiro.mostrar_tabuleiro()

            print(f'\n{tipo} ({tamanho} células):')

            orientacao = str(input('Introduz a orientação (H / V): '))
            posicao_inicial = str(input('Introduz a posição inicial: '))

            try:
                barco = Barco(tamanho, orientacao, posicao_inicial)


                if jogador.tabuleiro.colocar_barco(barco):
                    jogador.lista_barcos.append(barco)
                    verificacao = True
                    limpar_terminal()
                else:
                    print('\nBarco inválido, tenta novamente.')
                    os.system('pause')
                    limpar_terminal()
            except:
                print('\nBarco inválido, tenta novamente.')
                os.system('pause')
                limpar_terminal()
    
    print('\n✅ Tabuleiro introduzido com sucesso!\n')
    sleep(2)
    limpar_terminal()


def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# --------------
# INÍCIO AQUI
# --------------

limpar_terminal()

print('\n🚢 -- BATALHA NAVAL -- 🚢\n')
nome = input('O meu NOME: ')

nome = nome.upper()

jogador = Jogador(nome)
computador = Computador()

limpar_terminal()

print(f'Bem-Vindo, {nome}! :D')
sleep(2)
inserir_barcos_jogador(jogador)

print('O computador está a posicionar os seus barcos...')
computador.posicionar_barcos_random()
sleep(3)
print('\n✅ O computador está pronto!')
sleep(2)

turno_jogador = True

while True:
    if turno_jogador:
        limpar_terminal()

        print(f'--- Turno de {nome} ---')
        sleep(1)
        print(f'--- Pontos: {jogador.pontos}\n')
        sleep(2)

        print('O teu tabuleiro:')
        jogador.tabuleiro.mostrar_tabuleiro(visivel=True)

        print('\n')

        print('Tabuleiro do adversário:')
        computador.tabuleiro.mostrar_tabuleiro(visivel=False)


        resultado = jogador.efetuar_tiro(computador.tabuleiro)

        if resultado == 'acertou' or resultado == 'afundado':
            jogador.pontos += 1
        
        turno_jogador = False


        if computador.tabuleiro.todos_barcos_afundados():
            limpar_terminal()
            print(f'🎉 VITÓRIA! {nome} ganhou, parabéns! :D')
            break

    else:
        limpar_terminal()

        print('--- Turno do Computador ---')
        sleep(1)
        print(f'--- Pontos: {computador.pontos}\n')
        sleep(2)
        

        resultado = computador.efetuar_tiro(jogador.tabuleiro)

        if resultado == 'acertou' or resultado == 'afundado':
            turno_jogador = False
            computador.pontos += 1

        else:
            turno_jogador = True
        

        if jogador.tabuleiro.todos_barcos_afundados():
            limpar_terminal()
            print('💀 DERROTA! O computador ganhou! É assim a vida :v')
            break

    os.system('pause')