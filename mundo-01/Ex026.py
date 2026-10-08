Nome = str(input('Digite uma Frase: ')).strip().upper()
print(f'Nessa frase tem {(Nome.count('A'))} A' )
print(f'A letra a apareceu em {Nome.find('A')+1}')
print(f'A ultima letra a apareceu em {Nome.rfind('A')+1}')