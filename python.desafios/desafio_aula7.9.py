#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = (float(input('Digite seu salário: ')))
aumento = 15
valor_aumento = salario * 1.15
print('Seu novo salário é: {:.2f}'.format(valor_aumento))