numeros = []
while True:
    entrada = input(f'Digite um número (ou fim para terminar): ')
    if entrada.lower() == 'fim':
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim' para terminar.")
if numeros:
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
    print(f"A média dos números é: {media:.2f}")
else:
    print("Nenhum número foi inserido.")