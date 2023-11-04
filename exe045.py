import random
from time import sleep

print('-==-' *20)
print('Vamos jogar JOKENPÔ?')
print('-==-' *20)

jokenpon = ["Pedra", "Papel", "Tesoura"]

sleep(2)

escolha_pessoa = str(input('Pedra, Papel ou Tesoura? '))

escolha_pc = random.choice(jokenpon)

if escolha_pc == escolha_pessoa:
    print('Você escolheu {} e eu escolhi {} \nHouve empate!'.format(escolha_pessoa, escolha_pc))

elif escolha_pc == "Pedra":
    if escolha_pessoa == "Papel":
        print('Você escolheu {} e eu escolhi {} \nVocê venceu! Parabéns!'.format(escolha_pessoa, escolha_pc))
    elif escolha_pessoa == "Tesoura":
        print('Você escolheu {} e eu escolhi {} \nVocê perdeu!'.format(escolha_pessoa, escolha_pc))

elif escolha_pc == "Papel":
    if escolha_pessoa == "Pedra":
        print('Você escolheu {} e eu escolhi {} \nVocê perdeu!'.format(escolha_pessoa, escolha_pc))
    elif escolha_pessoa == "Tesoura":
        print('Você escolheu {} e eu escolhi {} \nVocê venceu! Parabéns!'.format(escolha_pessoa, escolha_pc))

elif escolha_pc == "Tesoura":
    if escolha_pessoa == "Pedra":
        print('Você escolheu {} e eu escolhi {} \nVocê venceu! Parabéns!'.format(escolha_pessoa, escolha_pc))
    elif escolha_pessoa == "Papel":
        print('Você escolheu {} e eu escolhi {} \nVocê perdeu!'.format(escolha_pessoa, escolha_pc))