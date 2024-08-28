numero = int(input('Digite um número para exibir sua tabuada: '))
for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')