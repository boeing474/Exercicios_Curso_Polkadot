numero = int(input('Digite um número: '))
def numero_perfeito(n):
    if n < 1:
        return False
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n


if numero_perfeito(numero):
    print(f'{numero} é um número perfeito.')
else:
    print(f'{numero} não é um número perfeito.')
