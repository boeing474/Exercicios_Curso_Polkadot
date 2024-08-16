soma = 0
print('Bem vindo! Digite os números que deseja somar, para parar de somar, digite 0')
while True:
    numero = int(input('Digite um número: '))

    if numero == 0:
        break
    else: soma += numero

print(f'A soma dos números digitados é {soma}')

