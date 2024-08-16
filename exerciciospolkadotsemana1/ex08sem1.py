numero = int(input('Digite um número e descubra se é Par ou Ímpar: '))
def impar_ou_par (numero):
    if numero % 2 == 0:
        return 'é Par'
    else:
        return 'É Ímpar'
print(impar_ou_par(numero))