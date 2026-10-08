frase = input('Diga seu nome: ').strip()

print(f'Seu nome em maiuscula {frase.upper()}')
print(f'Seu nome em minuscula {frase.lower()}')
print(f'Seu nome tem ao todo {len(frase) - frase.count(' ')}')
print(f'Seu primeiro nome tem {frase.find(' ')}')