import random
from time import sleep

print('-==-' *20)
print('Vamos jogar JOKENPÔ?')
print('-==-' *20)

jokenpon = ["Pedra", "Papel", "Tesoura"] # Criei uma lista com os elementos do jogo

sleep(2)

escolha_pessoa = str(input('Pedra, Papel ou Tesoura? '))

print('\n')

escolha_pc = random.choice(jokenpon) # A função que o computaor "escolhe" um dos elementos

if escolha_pc == escolha_pessoa:
    print('Você escolheu {} e eu escolhi {} \nHouve empate!'.format(escolha_pessoa, escolha_pc))

elif escolha_pc == "Pedra":
    if escolha_pessoa == "Papel":
        print('Você escolheu {} e eu escolhi {} \n\033[1;30;42mVocê venceu!\033[m Parabéns!'.format(escolha_pessoa, escolha_pc))
    elif escolha_pessoa == "Tesoura":
        print('Você escolheu {} e eu escolhi {} \n\033[1;30;43mVocê perdeu!\033[m'.format(escolha_pessoa, escolha_pc))
    else:
        print('JOGADA INVÁLIDA')

elif escolha_pc == "Papel":
    if escolha_pessoa == "Pedra":
        print('Você escolheu {} e eu escolhi {} \n\033[1;30;43mVocê perdeu!\033[m'.format(escolha_pessoa, escolha_pc))
    elif escolha_pessoa == "Tesoura":
        print('Você escolheu {} e eu escolhi {} \n\033[1;30;42mVocê venceu!\033[m Parabéns!'.format(escolha_pessoa, escolha_pc))
    else:
        print('JOGADA INVÁLIDA')

elif escolha_pc == "Tesoura":
    if escolha_pessoa == "Pedra":
        print('Você escolheu {} e eu escolhi {} \n\033[1;30;42mVocê venceu!\033[m Parabéns!'.format(escolha_pessoa, escolha_pc))
    elif escolha_pessoa == "Papel":
        print('Você escolheu {} e eu escolhi {} \n\033[1;30;43mVocê perdeu!\033[m'.format(escolha_pessoa, escolha_pc))
    else:
        print('JOGADA INVÁLIDA')

else:
    print('JOGADA INVÁLIDA')