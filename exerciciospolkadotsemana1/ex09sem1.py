frase = str(input('Digite uma frase aleatória: '))
letra = str(input('Qual letra gostaria de contar?: '))

print(f" A letra '{letra}' aparece {frase.lower().count(letra.lower())} vezes na sua frase.")