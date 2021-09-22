game = [[' ',' ',' '], 
        [' ',' ',' '],
        [' ',' ',' ']]


def board():
        print('\n\033[4m  | a | b | c \033[m')
        for count, row in enumerate(game):
                print(f'{count+1} |' + str(row).replace('[', ' ').replace(']','').replace(',', ' |').replace("'",""))
        print('-'*18)


def play(player, jogada):
        print(f'{player}, é sua vez:')
        while True:
                try:
                        coluna = str(input('Coluna (a, b ou c): '))
                        linha = int(input('Linha (1, 2 ou 3): '))
                        if coluna not in ['a', 'b', 'c'] or linha not in [1, 2, 3]:
                                print(f'\n\033[31mJogada inválida, tente novamente:\033[m')
                                continue
                        else:
                                coluna = int(coluna.replace('a','0').replace('b','1').replace('c','2'))
                except:
                        print(f'\n\033[31mJogada inválida, tente novamente:\033[m')
                        continue
                if game[linha-1][coluna] != ' ':
                        print(f'\n\033[31mJogada inválida, tente novamente:\033[m')
                        continue
                else:
                        game[linha-1][coluna] = jogada
                        break


def verif_vit(player, jogada):
        cg = 0
        for c in range(len(game)):
                if game[0][c] == game[1][c] == game[2][c] == jogada or\
                [jogada, jogada, jogada] in game or\
                game[0][0] == game[1][1] == game[2][2] == jogada or\
                game[2][0] == game[1][1] == game[0][2] == jogada:       
                        board()
                        print(f'\n\033[32m{player} venceu!\033[m\n')
                        return True
                elif game[c].count(' ') == 0:
                        cg += 1
        if cg == len(game):
                board()
                print(f'\n\033[32mDeu velha!\033[m\n')
                return True


print('-'*18)
print(f'{"JOGO DA VELHA":^18}')
print('-'*18)
p1 = str(input('\nJogador 1: '))
p2 = str(input('Jogador 2: '))

while True:
        board()
        play(p1, 'X')
        if verif_vit(p1, 'X'):
                break
        board()
        play(p2, 'O')
        if verif_vit(p2, 'O'):
                break