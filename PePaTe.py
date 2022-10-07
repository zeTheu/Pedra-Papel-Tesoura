import random
import time

#APRESENTAÇÃO DO JOGO
print('------------JO KEN PO------------')

print('\n[ 1 ]PEDRA \n[ 2 ]PAPEL \n[ 3 ]TESOURA')

#ESCOLHAS DA MÁQUINA E DO JOGADOR
escolha = int(input('\nQual você escolhe? '))
maquina = random.randrange(0, 4)
opcao = ['Pedra', 'Papel', 'Tesoura']

continuar = False
rejogar = 2   

#BLOCO DE ANDAMENTO DO JOGO
def jogada(mostra_opcao):
            
        print('Jogando... \n')
        time.sleep(1)
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO \n')
        time.sleep(1)
        if escolha == maquina:
            if escolha == 1:
                palavra = 'Pedra'
            elif escolha == 2:
                palavra = 'Papel'
            elif escolha == 3:
                palavra = 'Tesoura'
            print('Vocês escolheram {}'.format(palavra))
            print('JOGO EMPATADO')
        
        elif escolha == 1 and maquina == 2:
            print('Você escolheu {} e seu adversário escolheu {}'.format(mostra_opcao[0], mostra_opcao[1]))
            print('Papel embrulha pedra. \nVOCÊ PERDEU!')
        elif escolha == 1 and maquina == 3:
            print('Você escolheu {} e seu adversário escolheu {}'.format(mostra_opcao[0], mostra_opcao[2]))
            print('Pedra esmaga tesoura. \nVOCÊ GANHOU!')
        elif escolha == 2 and maquina == 1:
            print('Você escolheu {} e seu adversário escolheu {}'.format(mostra_opcao[1], mostra_opcao[0]))
            print('Papel embrulha pedra. \nVOCÊ GANHOU!')
        elif escolha == 2 and maquina == 3:
            print('Você escolheu {} e seu adversário escolheu {}'.format(mostra_opcao[1], mostra_opcao[2]))
            print('Tesoura corta papel. \nVOCÊ PERDEU!')
        elif escolha == 3 and maquina == 1:
            print('Você escolheu {} e seu adversário escolheu {}'.format(mostra_opcao[2], mostra_opcao[0]))
            print('Pedra esmaga tesoura. \nVOCÊ PERDEU!')
        elif escolha == 3 and maquina == 2:
            print('Você escolheu {} e seu adversário escolheu {}'.format(mostra_opcao[2], mostra_opcao[1]))
            print('Tesoura corta papel. \nVOCÊ GANHOU!')
        
jogada(opcao) 

#REPERGUNTAR SE QUER REPETIR
while not continuar:
    rejogar = int(input('\nVocê quer jogar novamente? \n1 = SIM \n2 = NÃO \n-> '))
    if rejogar == 2:
        continuar = True
        print('\nJOGO FINALIZADO!')
    else:
        print('\n[ 1 ]PEDRA \n[ 2 ]PAPEL \n[ 3 ]TESOURA')
        escolha = int(input('\nQual você escolhe? '))
        jogada(opcao)
        
#PEPATES