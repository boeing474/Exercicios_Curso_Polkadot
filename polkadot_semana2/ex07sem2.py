def calcular_media():
    total = 0
    somatorio = 0

    while True:
        notas = float(input('Digite suas notas, para parar digite -1: '))
        if notas == - 1:
            break
        total += notas
        somatorio += 1
    if notas == 0:
        print('Uau voce precisa estudar mais!')
    else:
        media = total / somatorio
        print(f'Sua média foi de {media}.')
calcular_media()
