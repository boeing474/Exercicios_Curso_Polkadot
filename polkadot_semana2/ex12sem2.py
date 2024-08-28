import random

def jogo():
    maquina = random.randint(1, 100)

    print('Vamos jogar um jogo?')
    print('Escolhi um número de 1 a 100, tente adivinhar, direi se está perto ou longe!')

    while True:
        tentativa = int(input('Escolha um número de 1 a 100!: '))

        if tentativa < 1 or tentativa > 100:
            print('Escolha somente número de 1 a 100!')
        elif tentativa < maquina:
            print('Está muito baixo, Digite outro número')
        elif tentativa > maquina:
            print('Está muito alto! Digite outro número')
        if tentativa == maquina:
            print('Uau você acertou!')
            break
if __name__ == '__main__':
    jogo()