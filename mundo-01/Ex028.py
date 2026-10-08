import random
Lista = [1,2,3,4,5]
escolha = random.choice(Lista)
Eu = int(input('Tente descobrir o numero que o computador pensou: '))
print(f'O numero do computador foi: {escolha}')
print(f'O meu numero foi {Eu}')
if escolha == Eu:
    print('Voce foi o vencedor')
else:
    print('Infelizmente voce perdeu')