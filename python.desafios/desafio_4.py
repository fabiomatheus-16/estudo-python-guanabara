#um programa que leia algo pelo teclado
#  e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

nome = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(nome)))
print('Está em minusculo? {}'.format(nome.islower()))
print('Está em maiusculo? {}'.format(nome.isupper()))
print('Está em numero? {}'.format(nome.isnumeric()))
print('Está em alfabetico? {}'.format(nome.isalpha()))