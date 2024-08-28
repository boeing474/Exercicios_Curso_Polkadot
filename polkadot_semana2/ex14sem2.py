def somar(n1,n2):
    return n1 + n2
def subtrair(n1,n2):
    return n1 - n2
def dividir(n1,n2):
    return n1 / n2
def multiplicar(n1,n2):
    return n1 * n2

def main():
    print('Bem vindo a calculadora!')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    print('Escolha o que deseja fazer!')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Dividir')
    print('4. Multiplicar')
    escolha = int(input('Digite o número que deseja: '))

    if escolha == 1:
        resultado = somar(n1,n2)
    elif escolha == 2:
        resultado = subtrair(n1,n2)
    elif escolha == 3:
        resultado = dividir(n1,n2)
    elif escolha == 4:
        resultado = multiplicar(n1,n2)
    elif escolha <= 5:
        resultado = 'Digite uma opção válida!'

    print(f'Seu resultado é {resultado}')

if __name__ == '__main__':
    main()