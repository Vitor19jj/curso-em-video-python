Viagem = float(input('Digite quantos km tem sua viagem? '))
if Viagem <= 200:
    v1 = (Viagem*0.50)
    print(f'O preco da sua viagem ficou de R${v1}')
else:
    v2 = (Viagem*0.45)
    print(f'O preco da sua viagem ficou de: R${v2}')