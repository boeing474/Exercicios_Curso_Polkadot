inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for numero in range(inicio, fim + 1):
    if primo(numero):
        print(numero)
