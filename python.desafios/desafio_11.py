#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM foram percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))

preco_dia = 60
preco_km = 0.15

total_diarias = dias * preco_dia
total_km = km * preco_km
total = total_diarias + total_km

print(f'Diárias: R${total_diarias:.2f}')
print(f'Km rodados: R${total_km:.2f}')
print(f'Total a pagar: R${total:.2f}')