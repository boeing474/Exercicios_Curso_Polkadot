def ordenar(n1,n2,n3):
    numeros = [n1,n2,n3]
    numeros.sort()
    return numeros
def main():
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um segundo número: '))
        num3 = float(input('Digite um terceiro número: '))

        numeros_ordem = ordenar(num1, num2, num3)

        print(f'Os números em ordem crescente que você digitou é {numeros_ordem}')

if __name__ == '__main__':
    main()