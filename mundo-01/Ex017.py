import math
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print (f'A soma dos catetos vai dar a hipotenusa media de {hi:.2f}')

co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print (f'A soma dos catetos vai dar a hipotenusa media de {hi:.2f}')
