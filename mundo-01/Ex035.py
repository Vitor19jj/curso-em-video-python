ps = float(input('Digite o primeiro segmento: '))
ss = float(input('Digite o segundo segmento: '))
ts = float(input('Digite o terceiro segmento: '))
if ps < ss + ts and ss < ps + ts and ts < ps + ss:
    print ('Os numeros acima podem formar um triangulo!')
else:
    print ('Os numeros acima nao podem formar um triangulo')