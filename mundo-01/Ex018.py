import math
angulo = float(input('Digite o angulo que voce deseja: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print(f'O angulo de {angulo:.1f} tem o seno de {seno:.2f}')
print(f'O angulo de {angulo:.1f} tem o cosseno de {cosseno:.2f}')
print(f'O angulo de {angulo:.1f} tem o tangente de {tangente:.2f}')