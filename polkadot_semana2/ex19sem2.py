
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
peso1 = 2
peso2 = 3
peso3 = 5

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f'A média ponderada das notas é: {media_ponderada:.2f}')
