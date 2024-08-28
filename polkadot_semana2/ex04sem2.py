frase = str(input('Digite uma frase para verificar se é um palíndromo: ')).lower().replace(' ', '')
frase_invertida = frase[: : -1]

if frase_invertida == frase:
    print('É palíndromo')
else:
    print('Não é palíndromo')
