## Calculadora em python

print(" Selecione o número da operação desejada: \n 1 - soma \n 2 - subtração \n 3 - divisão \n 4 - multiplicação ")

x = int(input(" Selecione o tipo de operação..:"))
x1 = int(input(" Digite um número..........:"))
x2 = int(input(" Digite outro número.......:"))

if x == 1:
    soma = x1 + x2
    print("O resultado da soma é...: {}".format(soma))
if x == 2:
    subtracao = x1 - x2
    print("O resultado da subtração é...: {}".format(subtracao))
if x == 3:
    divisao = x1 / x2
    print("O resultado da divisão é...: {}".format(divisao))
if x == 4:
    multiplicacao = x1 * x2
    print("O resultado da multriplicação é...: {}".format(multiplicacao))