#Exercício Python 12: Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

produto = (float(input('Preço do produto: ')))
desconto = 5
valor_desconto = produto * (desconto / 100)
preco_final = produto - valor_desconto
print('Preço com desconto de 5% totaliza: {}'.format(preco_final))