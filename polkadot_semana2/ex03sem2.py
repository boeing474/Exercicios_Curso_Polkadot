print('Bem vindo! Digite o seu peso e sua altura para calcular seu IMC!')
peso = float(input('Digite o seu peso em kilogramas: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura * altura)

print(f'O seu IMC é de {imc}')