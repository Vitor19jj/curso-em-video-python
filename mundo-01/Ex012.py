Produto = float(input('Qual o valor do produto que voce quer? R$'))
desconto = Produto - (Produto*5/100)
print(f'O produto com o desconto de 5% fica de R${desconto:.1f}')
