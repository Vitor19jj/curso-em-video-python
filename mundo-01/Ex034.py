Salario = float(input('Qual seu salario? '))
if Salario <= 1250:
    NValor = Salario + (Salario*10/100)
    print(f'O seu novo salario e de: R${NValor:.2f}')
else:
    NNValor = Salario + (Salario*15/100)
    print(f'O seu novo salario e de: R${NNValor:.2f}')