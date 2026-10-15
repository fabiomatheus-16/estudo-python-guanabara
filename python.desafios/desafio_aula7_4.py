#Exercício Python 8: Escreva um programa
#que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = (int(input('Escreva o valor em metros: ')))
n2 = n1 * 100
n3 = n1 * 1000
print('O valor em metros tem: {}, em centimetros tem: {}, e em milimetros tem: {}'.format(n1,n2,n3))