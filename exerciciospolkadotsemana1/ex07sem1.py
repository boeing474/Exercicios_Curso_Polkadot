compras = ['arroz','leite','macarrão']

print('\nLista de Compras:')
for i, item in enumerate(compras, start = 1):
        print(f'{i}. {item}')
while True:
    item = input(f'Deseja adiconar algo? Se não, digite "sair" \n').lower()
    if item == 'sair':
        print('Até a próxima!')
        break

    else: compras.append(item)
    print('Item adicionado com sucesso!')
    print('\nLista de Compras:')
    for i, item in enumerate(compras, start=1):
        print(f'{i}. {item}')
