
def somar():
    soma = 0
    for n in range (1, 101):
        if n % 2 == 0:
          soma += n
    return soma
def main():
    total = somar()
    print(f'A soma dos números pares, entre 1 e 100 é de {somar()}')

if __name__ == '__main__':
    main()