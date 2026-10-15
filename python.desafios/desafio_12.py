#Desafio 12, digitar um número e retornar o valor somente inteiro.

import math
valor = (float(input('Digite um valor: ')))
n1 = math.trunc(valor) 
print(f'O valor é {valor} e tem a parte inteira {n1}')
