def contar_vogais(frase):
    vogais = 'aeiou'
    total_vogais= 0
    for letra in frase:
        if letra in vogais:
            total_vogais += 1
    return total_vogais
frase = str(input('Digite uma frase e descubra quantas vogais tem!: '))

numero_de_vogais = contar_vogais(frase)
print(f'A frase contem {numero_de_vogais} vogais.')