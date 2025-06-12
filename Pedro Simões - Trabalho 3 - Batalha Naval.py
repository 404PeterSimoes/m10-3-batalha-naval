# Batalha Naval - Pedro Simões

class Barco:
    def __init__(self, tamanho: int, orientacao: str, posicao_inicial: str):
        self.tamanho = tamanho
        self.orientacao = orientacao.upper()
        self.posicao_inicial = posicao_inicial.upper()
        self.coordenadas_ocupadas = self.calc_CoordenadasOcupadas()
        self.posicoes_atingidas = []

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

    # Verificar se o barco está completamente afundado
    def verificar_esta_afundado(self) -> bool:
        return len(self.posicoes_atingidas) == self.tamanho

    def barco_receber_tiro(self, coord: str) -> bool:

        # Verificar se a coordenada introduzida estiver a ser ocupada por um barco
        if coord in self.coordenadas_ocupadas:

            # Verificar se a coordenada não foi atingida
            if coord not in self.posicoes_atingidas:
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
 
    def tabuleiro_receber_tiro(self, coord: str):
        # Colocar esta antes de executar a funcao: coord = coord.upper()

        # Verificar se a coordenada recebida já foi atacada
        if coord in self.tiros_recebidos:
            return 'ja_atacado' # Pode se colocar no futuro verdadeiro ou falso
        
        self.tiros_recebidos.append(coord)

        # Verificar se acertou algum barco
        for barco in self.barcos:
            if barco.barco_receber_tiro(coord):

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
                celula = self.grelha[i][j]

                if not visivel and celula == 'B':
                    linha_valores.append('~')
                else:
                    linha_valores.append(celula)

            print(f'{letra} {' '.join(linha_valores)}')

    # Verificar se todos os barcos estão afundados    
    def todos_barcos_afundados(self) -> bool:

        for barco in self.barcos:
            if barco.esta_afundado() == False:
                return False
        
        return True


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.tabuleiro = Tabuleiro()
        self.lista_barcos = []

    def efetuar_tiro(self, tabuleiro_adversario: Tabuleiro):

        # Ciclo "infinito"
        while True:
            try:
                coord = input(f'\n{self.nome}, introduz uma coordenada para disparar: ').upper()

                #Validar o formato da coordenada
                if len(coord) != 2 or ord(coord[0]) < 65 or ord(coord[0]) > 74 or not coord[1].isdigit():
                    print('\nErro! Coordenada inválida.\nTenta novamente:')
                    continue

                resultado = tabuleiro_adversario.tabuleiro_receber_tiro(coord)

                if resultado == "ja_atacado":
                    print("Já atacaste essa posição! Tenta outra.")
                    continue
                elif resultado == "acertou":
                    print("🎯 Acertaste num barco inimigo!")
                elif resultado == "afundado":
                    print("💥 Acertaste e afundaste um barco inimigo!")
                elif resultado == "falhou":
                    print("Falhaste!")

                return resultado

            except:
                print('\nErro! Coordenada inválida.\nTenta novamente:')


def inserir_barcos_jogador():
    tabuleiro_jogador.mostrar_tabuleiro()

    print('\n--- Inserir Barcos ---')

    # ---------------------------------------------------

    verificacao = False

    while not verificacao:
        print('\nPorta-avião (5 células):\n')

        orientacao = str(input('Introduz a orientação ( H / V ): '))
        posicao_inicial = str(input('Introduz a posição inicial: '))

        porta_aviao1 = Barco(5, orientacao, posicao_inicial)

        if tabuleiro_jogador.colocar_barco(porta_aviao1):
            verificacao = True
        else:
            print('\nErro! Esse barco não é válido.\nTenta novamente:')
            tabuleiro_jogador.mostrar_tabuleiro()
        
    tabuleiro_jogador.mostrar_tabuleiro()

    # ---------------------------------------------------

    verificacao = False

    while not verificacao:
        print('\nCruzador (4 células):\n')

        orientacao = str(input('Introduz a orientação ( H / V ): '))
        posicao_inicial = str(input('Introduz a posição inicial: '))

        cruzador1 = Barco(4, orientacao, posicao_inicial)

        if tabuleiro_jogador.colocar_barco(cruzador1):
            verificacao = True
        else:
            print('\nErro! Esse barco não é válido.\nTenta novamente:')
            tabuleiro_jogador.mostrar_tabuleiro()
        
    tabuleiro_jogador.mostrar_tabuleiro()

    # ---------------------------------------------------

    verificacao = False
    
    while not verificacao:
        print('\nContratorpedeiro (3 células):\n')

        orientacao = str(input('Introduz a orientação ( H / V ): '))
        posicao_inicial = str(input('Introduz a posição inicial: '))

        contratorped1 = Barco(3, orientacao, posicao_inicial)

        if tabuleiro_jogador.colocar_barco(contratorped1):
            verificacao = True
        else:
            print('\nErro! Esse barco não é válido.\nTenta novamente:')
            tabuleiro_jogador.mostrar_tabuleiro()

    tabuleiro_jogador.mostrar_tabuleiro()

    # ---------------------------------------------------

    verificacao = False

    while not verificacao:
        print('\nContratorpedeiro (3 células):\n')

        orientacao = str(input('Introduz a orientação ( H / V ): '))
        posicao_inicial = str(input('Introduz a posição inicial: '))

        contratorped2 = Barco(3, orientacao, posicao_inicial)

        if tabuleiro_jogador.colocar_barco(contratorped2):
            verificacao = True
        else:
            print('\nErro! Esse barco não é válido.\nTenta novamente:')
            tabuleiro_jogador.mostrar_tabuleiro()

    tabuleiro_jogador.mostrar_tabuleiro()

    # ---------------------------------------------------

    verificacao = False

    while not verificacao:
        print('\nSubmarino (2 células:)\n')

        orientacao = str(input('Introduz a orientação ( H / V ): '))
        posicao_inicial = str(input('Introduz a posição inicial: '))

        submarino1 = Barco(2, orientacao, posicao_inicial)

        if tabuleiro_jogador.colocar_barco(submarino1):
            verificacao = True
        else:
            print('\nErro! Esse barco não é válido.\nTenta novamente:')
            tabuleiro_jogador.mostrar_tabuleiro()

    tabuleiro_jogador.mostrar_tabuleiro()

    # ---------------------------------------------------

    verificacao = False

    while not verificacao:
        print('\nSubmarino (2 células:)\n')

        orientacao = str(input('Introduz a orientação ( H / V ): '))
        posicao_inicial = str(input('Introduz a posição inicial: '))

        submarino2 = Barco(2, orientacao, posicao_inicial)

        if tabuleiro_jogador.colocar_barco(submarino2):
            verificacao = True
        else:
            print('\nErro! Esse barco não é válido.\nTenta novamente:')
            tabuleiro_jogador.mostrar_tabuleiro()

    tabuleiro_jogador.mostrar_tabuleiro()
    print('\nTabuleiro introduzido com sucesso!\n')

# --------------
# INÍCIO AQUI
# --------------

tabuleiro_jogador = Tabuleiro()
tabuleiro_maquina = Tabuleiro()

print('\n🚢 -- BATALHA NAVAL -- 🚢\n')
nome = input('O meu NOME: ')

inserir_barcos_jogador()

# jogador = Jogador(nome, tabuleiro1, barcos)

