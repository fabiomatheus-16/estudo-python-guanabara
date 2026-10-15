#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar. 

d = (float(input('Quanto de dinheiro você tem em real? ')))
dolar = d / 4.99
print('Com R${} você pode comprar US${:.2f}'.format(d, dolar))
print('Seu dinheiro convertido em dolar fica: US${}'.format(d * 4.99)) 